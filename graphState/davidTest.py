from cqc.pythonLib import CQCConnection, qubit

def main():
    with CQCConnection("David") as david:
        # receive qubit D from Charlie
        qd = david.recvQubit()
        print("David: received qubit D from Charlie")

        # prepare a new qubit E in ths state |+>
        qe = qubit(david)
        qe.H()
        print("David: prepared a new qubit E in the state |+>")

        # expand the graph state on qubit D and E
        qd.cphase(qe)
        print("David: expanded the graph state on qubit D and E")

        # send qubit E to Bob
        david.sendQubit(q=qe, name="Charlie")
        print("David: sent qubit E to Charlie")

        # perform operation exp(iPI/4 Z) on qubit D
        # (one of the operations to induced a local complementation at E)
        # exp(iPI/4 Z) = rotate -PI/2 around Z-axis = rotate 3PI/2 around Z-axis
        # 3PI / 2  = 192 steps
        qd.rot_Z(192)
        print("David: performed operation exp(iPI/4 Z) on qubit D")

        # receive measurement outcome of qubit E from Charlie
        result_e = ord(david.recvClassical(timout=5).decode()[0])
        # result_e = int(david.recvClassical(timout=5).decode())
        print("David: received the measurement outcome of E from Charlie, outcome = "+str(result_e))

        # apply Z operation to qubit D if the measurement out was 1 and nothing if it's 0
        if result_e == 1:
            qd.Z()
            print("David: applied Z operation to qubit D")
        else:
            print("David: does nothing on qubit D since the measurement outcome was 0")

        # measure qubit D in X-basis
        qd.H()
        result_d = qd.measure()
        print("David: David's outcome was "+str(result_d))

main()