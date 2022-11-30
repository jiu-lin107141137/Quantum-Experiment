## The BB84 QKD(Quantum key distribution) Protocol

### Basic Steps :
Now suppose that there are 2 nodes, Alice and Bob, want to make there own secret shared key.

1. Alice first prepares 3 things: 
    ```
        1. (4+k)n qubits which state are |0>
        2. a random base(comsists of 0 and 1) of (4+k)n length
        3. a random key(comsists of 0 and 1) of (4+k)n length
    ```
2. Alice performes X-gate on each qubit if the corresponding bit of base is 1 
3. Alice perfromes Hadamard-gate on each qubit if the corresponding bit of key is 1 
    Now, each qubit is in one of the four states,  
    ```
        |0>, |1>, |+> and |->
    ```
    To become a specific state, the 4 states stand the same probability, **25%**.  
    base[i] determines a qubit to be |0> or |1>, while key[i] determines a qubit to be in the basis od X or Z  
    > 
    **Note: The four states are not all mutually orthogonal, and therefore no measurement can distinguish between (all of) them with certainty**
    >
4. Alice sends the qubits to Bob
5. Alice and Bob discard any bits where Bob measures a different basis than Alice prepared.
    1. Bob receives the qubits, and prepares a guessing base(gb) of (4+k)n length
    2. Bob measures the qubits in Z-basis if the corresponding bit of gb is 0 and in X-basis if gb is = 1, then stores the measurement results<br>
    3. Bob send the gb to Alice
    4. Alice receives the gb, and commpares the guessing base from Bob and the base of Alice
    5. Alice gets an array of indices where gb[i] = base[i], discard corresponding key if the index is not in the array
    6. Alice sends the array to Bob, Bob receives it and discards the measurements if the corresponding index is not in the array
        >
        **This means the qubits are measured by Bob in different basis than Alice prepared.**
        >
    After doing this, with high probability, there will be at least 2n bits left.  
    For Alice, the 2n bits is the key, For Bob, is the measurement.  
    The key and measurements should be the same if there're no coherences in the channel and no eavesdropping during the teleporting  
6. Alice randomly selects a subset of n bits that will to serve as a check on others' eavesdropping and noise, and tells Bob which bits she selected.
    1. Alice randomly picks n indices, sends them to Bob
7. Alice and Bob announce and compare the values of the n check bits. If more than an acceptable number disagree, they abort the protocol.
    1. Bob receives the indices, sends corresponding bits from measurements to Alice
    2. Alice receives the bits from Bob, compared them with corresponding checking bits of Alice, and records the QBER.
    3. Based on the QBER, Alice tells Bob if the QKD is successful or not.<br>
       => if successful, now Alice and Bob have the same key(the bits where the indices weren't picked to compare)  
       => if fail, redo the protocol
8. Alice and Bob perform information reconciliation and privacy amplification on the remaining n bits to obtain m shared key bits.

### What will happen when the communicating is under disruption :
Now let's consider this protocol to be performed **in reality**, there will be certain noise in the communicating channel and others' eavesdropping during the communicating. These disruptions will cause the information an idle qubit holds to fade away, result in the measurement is not the one expects.  
Look at the step 4, since Alice only sends qubits to Bob, the basis to measure qubits has not been revealed, eavesdropper has no idea which basis to measure in to eavesdrop on the communication; at best, he can only guess, and if his guess was wrong, he will disturbed the state sent to Bob.  
If the state is disturbed by noise or eavesdropping, Bob will receive the wrong measurement with high probability, and this will be discovered by Bob and Alice in step 7.

### References: 
Michael A. Nielsen, Isaac L. Chuang, Massachusetts Institute of Technology. (December 2010). Quantum Computation and Quantum Information(10th Anniversary Edition). Cambridge University Press, New York.
