"""
prob_41.py

Description: 

Donald MacIntyre - djm4912
"""

import math
import itertools

def isPrime(n):
    s = math.sqrt(n)
    for i in xrange(2,n):
        if (n % i == 0):
            return False
        if i > s:
            break
    return True

def genPandigit():
    l = []
    t = []
    for i in xrange(1,10):
        c = i
        e = ""
        while c > 0:
            e += str(c)
            c -= 1
        l = list(itertools.permutations(e))
        for i in l:
            test = ""
            for j in i:
                test += j
            t.append(int(test))
    return t
            

def main() :
    t = genPandigit()
    pap = []
    print(2143 in t)
    for i in t:
        if isPrime(i) == True:
            pap.append(i)
    print(max(pap))
            

if __name__ == "__main__":
    main()
