"""
prob_46.py

Description: 

Donald MacIntyre - djm4912
"""

import math

def isPrime(n):
    s = math.sqrt(n)
    for i in xrange(2,n):
        if (n % i == 0):
            return False
        if i > s:
            break
    return True

def primesLessThanN(n):
    l = []
    for i in range(2,n):
        if isPrime(i):
            l.append(i)
    return l

def genValidTwiceASquare(n):
    l = []
    s = 1
    while True:
        l.append(2*(s**2))
        if l[-1] > n:
            break
        s += 1
    return l

def main() :
    i = 5777
    while True:
        if isPrime(i) == False: # number is composite
            flag = False
            #attempt to write as a sum of prime and twice a square
            l = primesLessThanN(i)
            for j in l:
                for x in genValidTwiceASquare(i):
                    if x + j == i:
                        flag == True
                        break
        print(i,flag)
        i += 2
        if flag == False:
            break
    print(i-2)

if __name__ == "__main__":
    main()
