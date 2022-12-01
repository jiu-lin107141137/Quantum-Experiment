from cqc.pythonLib import CQCConnection, qubit

def main():
    with CQCConnection("Alice") as alice:
        # prepare 2 qubits in the state | 0 >
        qa = qubit(alice)
        qb = qubit(alice)
        print("Alice: 2 qubits prepared")

        # turn the qubits into state | + >
        qa.H()
        qb.H()
        print("Alice: turned 2 qubits into state |+>")

        # make 2 qubits graph state by performing CPHASE operation between A and B
        # A is the control qubit, while B is the target
        qa.cphase(qb)
        print("Alice: made 2 qubit graph state")

        # send qubit B to Bob
        alice.sendQubit(q=qb, name="Bob")
        print("Alice: sent qubit B to Bob")

        # measure qubit A in X-basis
        qa.H()
        result_a = qa.measure()
        print("Alice: Alice's outcome was "+str(result_a))

# print("")
main()