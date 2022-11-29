from cqc.pythonLib import CQCConnection, qubit
import random
import time
import math
from globals import globals

globalVariables = globals()

def main() :
  base = "".join(random.choices(population=["0", "1"], k=globalVariables.cap))
  key_origin = "".join(random.choices(population=["0", "1"], k=globalVariables.cap))

  with CQCConnection("Alice") as Alice:
    # send qubits to Bob
    for i in range(globalVariables.cap):
      q = qubit(Alice)
      if key_origin[i] == '1' : 
        q.X()
      if base[i] == '1' :
        q.H()
      Alice.sendQubit(q, "Bob")
      if i % 10 == 9:
        print("sent "+str(i+1))
      time.sleep(.5)

    # receive base from Bob
    base_guess = Alice.recvClassical(msg_size=4096).decode()
    print("Alice received guessing base")

    key_correct_index = ""
    key_correct = ""
    
    # compare the bases of Alice and Bob
    for i in range(globalVariables.cap):
      if base_guess[i] == base[i]:
        key_correct += key_origin[i]
        key_correct_index += str(i)+" "
    
    # send the correct base to Bob
    print("Alice sent correct base")
    Alice.sendClassical("Bob", key_correct_index.encode())
    time.sleep(.2)

    # decide the indices of key to compare
    l = math.ceil(len(key_correct) / 2)
    compare_index = random.sample(range(len(key_correct)), l)
    compare_index.sort()
    key_compare = ""
    key_final = ""

    ptr = 0

    # split the key into the one going to be compared 
    # and the one going to be the final key
    for i in range(len(key_correct)):
      if ptr < l and i == compare_index[ptr]:
        key_compare += key_correct[i]
        ptr += 1
      else:
        key_final += key_correct[i]
    
    # send Bob the indices to compare
    print("Alice sent indices to compare")
    Alice.sendClassical("Bob", "".join(str(pos)+" " for pos in compare_index).encode())
    time.sleep(1)
    # receive the values of indices
    bob_key_compare = Alice.recvClassical(msg_size=4096).decode()
    print("Alice received compared values")
    # check qubit error rate
    err_count = 0
    for i in range(len(bob_key_compare)):
      if bob_key_compare[i] != key_compare[i]:
        err_count += 1
    print("err_count: "+str(err_count))
    print("Qber: "+str(err_count * 1. / len(key_compare)))
    print("A: "+str(len(key_final)))
    print("A: "+key_final)

    if err_count * 1. / len(key_compare) <= globalVariables.qber:
      Alice.sendClassical("Bob", "success".encode())
    else:
      Alice.sendClassical("Bob", "failed".encode())


print("")
main()