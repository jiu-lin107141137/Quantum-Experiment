from cqc.pythonLib import CQCConnection, qubit

def main():
    with CQCConnection("Bob") as bob:
        # receive qubit B from Alice
        qb = bob.recvQubit()
        print("Bob: received qubit B from Alice")

        # create a new qubit C in the state |+>
        qc = qubit(bob)
        qc.H()
        print("Bob: created a new qubit C in the state |+>")

        # expand the graph state
        qb.cphase(qc)
        print("Bob: expanded the graph state on B and C")

        # perform operation exp(iPI/4 Z) on qubit B 
        # exp(iPI/4 Z) == rotate -PI/2 around Z-axis, i.e. rotate 3PI/2 around Z-axis
        # (one of the operations to induced a local complementation at C)
        # 1 step = 2PI/256
        # 192 steps = 3PI/2
        qb.rot_Z(192)
        print("Bob: performed operation exp(iPI/4 Z) on qubit B")

        # send qubit C to Charlie
        bob.sendQubit(q=qc, name="Charlie")
        print("Bob: sent qubit C to Charlie")

        # measure the qubit B in the Z-basis
        result_b = qb.measure()
        print("Bob: Bob's outcome was "+str(result_b))

main()