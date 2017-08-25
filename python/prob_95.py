"""
prob_95.py

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
    l = 1
    s = math.sqrt(n)
    for i in xrange(2,n):
        if (n % i == 0):
            l += i
            l += n / i
        if i > s:
            break
    return l

def genChain(n):
    l = []
    l.append(n)
    while True:
        s = factors(l[-1])
        if s > 1000000:
            return -1
        l.append(s)
        if len(set(l)) != len(l):
            return l[:-1]

def main() :
    m = 0
    for i in xrange(1,1000000):
        l = genChain(i)
        if l != -1:
            if len(l) > m:
                s = min(l)
                m = len(l)
    print(s)
    print(m)

if __name__ == "__main__":
    main()
