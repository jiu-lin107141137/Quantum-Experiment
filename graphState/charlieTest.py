from cqc.pythonLib import CQCConnection, qubit

def main():
    with CQCConnection("Charlie") as charlie:
        # receive qubit C from Bob
        qc = charlie.recvQubit()
        print("Charlie: received qubit C from Bob")

        # create a new qubit D in the state |+>
        qd = qubit(charlie)
        qd.H()
        print("Charlie: prepared a new qubit D in the state |+>")

        # expand the graph state
        qc.cphase(qd)
        print("Charlie: expand the graph state on C and D")

        # perform operation exp(-iPI/4 X) and exp(iPI/4 Z) on qubit C and D respectively
        # (two of the operations to induced a local complementation at C)
        # exp(-iPI/4 X) = rotate PI/2 around X-axis
        # PI/2 = 64 steps
        # exp(iPI/4 Z) = rotate -PI/2 around Z-axis = rotate 3PI/2 around Z-axis
        # 3PI/2 = 192 steps
        qc.rot_X(64)
        qd.rot_Z(192)
        print("Charlie: performed exp(-iPI/4 X) and exp(iPI/4 Z) on qubit C and D respectively")

        # send qubit D to David
        charlie.sendQubit(q=qd, name="David")
        print("Charlie: sent qubit D to David")

        # receive qubit E from David
        qe = charlie.recvQubit()
        print("Charlie: received qubit E from David")

        # expand the graph state on qubit E and D
        qe.cphase(qc)
        print("Charlie: expanded the graph state on qubit E and C")

        # perform operation exp(-iPI/4 X) and exp(iPI/4 Z) on qubit E and C respectively
        # (two of the operations to induced a local complementation at E)
        # exp(-iPI/4 X) = rotate PI/2 around X-axis
        # PI/2 = 64 steps
        # exp(iPI/4 Z) = rotate -PI/2 around Z-axis = rotate 3PI/2 around Z-axis
        # 3PI/2 = 192 steps
        qe.rot_X(64)
        qc.rot_Z(192)
        print("Charlie: performed exp(-iPI/4 X) and exp(iPI/4 Z) on qubit E and C respectively")

        # measure qubit E in Z-basis
        result_e = qe.measure()
        print("Charlie: measured qubit E, outcome was: "+str(result_e))

        # perform Z operation to qubit C if the outcome of E was 1 and does nothing if it was 0
        if result_e == 1:
            qc.Z()
            print("Charlie: applied Z operation to qubit C")
        else:
            print("Charlie: does nothing on qubit C since the measurement outcome was 0")

        # send the measurement outcome to David
        print("Charlie: sent the measurement outcome of qubit E to David")
        charlie.sendClassical(msg=("1".encode() if result_e == 1 else "0".encode()), name="David")

        # measure qubit C in X-basis
        qc.H()
        result_c = qc.measure()
        print("Charlie: Charlie's outcome was "+str(result_c))

main()