## The BB84 QKD(Quantum key distribution) protocol
<br>
#### Steps
<br>
Now consider that there are 2 nodes, Alice and Bob, want to make there own secret shared key.
<br>
1. Alice first prepared 3 things:<br>
    (4+k)n qubits which state are |0>,<br>
    a random base(comsists of 0 and 1) of (4+k)n length<br>
    a random key(comsists of 0 and 1) of (4+k)n length<br>
2. Alice performed X-gate on Qi if base[i] = 1<br>
3. Alice perfromed Hadamard-gate on Qi if key[i] = 1<br>
Now, each qubit is in the 1 of the 4 states, <br>
    |0>, |1>, |+>, |->, <br>
to become a specific state, the 4 states stand the same probability, 25%.<br>
base[i] determined a qubit to be |0> or |1>, <br>
and the key[i] determined a qubit to be in the basis od X or Z
** the four states are not all mutually orthogonal, and therefore no measurement can distinguish between (all of) them with certainty **