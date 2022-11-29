from cqc.pythonLib import CQCConnection
import random
import time
from globals import globals

globalVariables = globals()

def main() :
  base_guess = "".join(random.choices(population=["0", "1"], k=globalVariables.cap))
  key_guess = ""

  with CQCConnection("Bob") as Bob:
    # receive qibits from Alice
    for i in range(globalVariables.cap):
      q = Bob.recvQubit()
      if base_guess[i] == '1':
        q.H()
      key_guess += str(q.measure())
      
      time.sleep(.5)

    print("Bob sent guessing base")
    Bob.sendClassical("Alice", base_guess.encode())
    time.sleep(1)

    # receive the correct indices of base
    key_correct_index = []
    key_correct = ""
    
    for token in Bob.recvClassical(msg_size=4096).decode().split(" "):
      if token != "":
        key_correct_index.append(int(token))
    for ind in key_correct_index:
      key_correct += key_guess[ind]
    print("Bob received correct base")

    time.sleep(1)

    # receive the indices to compare and
    # split the key into 2 parts
    # one is going to be compared, 
    # while the other one is going to be the final key
    compare_index = []
    key_compare = ""
    key_final = ""
    for pos in Bob.recvClassical(msg_size=4096).decode().split(" "):
      if pos != "":
        compare_index.append(int(pos))
    print("Bob received indices to compare")

    ptr = 0
    l = len(compare_index)

    for i in range(len(key_correct)):
      if ptr < l and i == compare_index[ptr]:
        key_compare += key_correct[i]
        ptr += 1
      else:
        key_final += key_correct[i]


    # send Alice the values of indices to compare
    print("Bob sent compared values")
    Bob.sendClassical("Alice", key_compare.encode())
    time.sleep(.5)
    
    # receive the result of bb84
    result = Bob.recvClassical().decode()
    if result == "success":
      print("success")
    else:
      print("failed")

    print("B: "+str(len(key_final)))
    print("B: "+key_final)
main()