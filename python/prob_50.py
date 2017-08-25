"""
prob_50.py

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

def genPrime(p):
    t = []
    for i in xrange(1,p+1):
        if isPrime(i):
            t.append(i)
    return t

def main() :
    g = genPrime(50)
    m = 0
    for i in range(len(g)):
        s = 0
    
if __name__ == "__main__":
    main()
