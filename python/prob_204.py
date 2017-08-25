"""
prob_204.py

Description: 

Donald MacIntyre - djm4912
"""

import time
import math

def isPrime(n):
    s = math.sqrt(n)
    if n == 1:
        return False
    for i in xrange(2,n):
        if (n % i == 0):
            return False
        if i > s:
            break
    return True

def factors(n):
    l = [1,n]
    s = math.sqrt(n)
    for i in xrange(2,n):
        if (n % i == 0):
            l.append(i)
            l.append(n / i)
        if i > s:
            break
    return set(l)

def isHamming(g,n):
    f = factors(n)
    for i in f:
        if i > g and isPrime(i):
            return False
    return True

def main() :
    st = time.clock()
    s = 0
    for i in xrange(1,(10**9)+1):
        if isPrime(i) == False or i < 10:
            if isHamming(100,i):
                s += 1
    print(s)
    print(time.clock()-st)

if __name__ == "__main__":
    main()
