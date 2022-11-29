## The BB84 QKD(Quantum key distribution) protocol

### Steps
Now consider that there are 2 nodes, Alice and Bob, want to make there own secret shared key.

1. Alice first prepared 3 things:<br>
    ```
        1. (4+k)n qubits which state are |0>
        2. a random base(comsists of 0 and 1) of (4+k)n length
        3. a random key(comsists of 0 and 1) of (4+k)n length
    ```
2. Alice performed X-gate on Qi if base[i] = 1<br>
3. Alice perfromed Hadamard-gate on Qi if key[i] = 1<br>
    Now, each qubit is in one of the four states, <br>
    ```
        |0>, |1>, |+> and |->
    ```
    To become a specific state, the 4 states stand the same probability, **25%**.<br>
    base[i] determined a qubit to be |0> or |1>, <br>
    and the key[i] determined a qubit to be in the basis od X or Z<br>
    > 
    **Note: The four states are not all mutually orthogonal, and therefore no measurement can distinguish between (all of) them with certainty**
    >
4. Alice sent the qubits to Bob
5. Bob received the qubits, and prepared a guessing base(gb) of (4+k)n length
6. Bob measured the qubits in Z-basis if the gb[i] = 0 and in X-basis if the gb[i] = 1, then stored the results<br>
7. Bob sent the gb to Alice
8. Alice received the gb, and commpared the guessing base and the base
9. Alice got a array of indices where gb[i] = base[i], discard key[i] if i is not in the array
10. Alice sent the indices to Bob, Bob received it and discard the measurements[i] if i is in the indices
    >
    **This means the qubits are measured by Bob in different basis than Alice prepared.**
    >
    After doing this, with high probability, there would be at least 2n bits left.<br>
    For Alice, the 2n bits is the key, For Bob, is the measurement, <br>
    the key and measurements should be the same if there're no coherences in the channel and no eavesdropping during the teleporting<br>
    <br>
    Let's define the key of Alice as k1, and the measurement of Bob as k2
11. Alice randomly picked n indices, sent them to Bob
12. Bob received the indices, sent k2[i] to Alice if i is in the indices
13. Alice received the half of k2, compared k1[i] and k2[i], recorded the QBER.
14. based on the QBER, Alice told Bob if the QKD is successful or not.<br>
    if success, now Alice and Bob would have the same key(the bits where the indices weren't picked to compare)<br>
    if failed, redo the protocol
