"""
print ("A: " + str(A))
"""

import math

def PathTheorem(Side1, Side2, NumbOfDec = 2):
    C =  round(math.sqrt(Side1 * Side1 + Side2 * Side2), NumbOfDec)
    Side1 = Side1 + 1
    return C

# poop
def Main():
    A = int(input("A --> "))
    B = int(input("B --> "))
    print ("A: " + str(A))
    print ("B: " + str(B))
    C =  PathTheorem (A, B)
    print ("C: " + str(C))

Main()
