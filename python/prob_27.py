"""
prob_27.py

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

def calcNumberofPrimes(a,b):
    n = 0
    cons_prime = 0
    while True:
        e = (n * n) + (a*n) + b
        if e > 0:
            if isPrime((n * n) + (a*n) + b):
                cons_prime += 1
                n += 1
            else:
                return cons_prime
        else:
            return cons_prime

def main() :
    m = 0
    index = []
    for i in xrange(-1000, 1001):
        for j in xrange(3,1001,2):     # b must be positive and prime
            curr = calcNumberofPrimes(i,j)
            if  curr > m:
                m = curr
                index = [i,j,i * j]
    print(index)
    print(m)

if __name__ == "__main__":
    main()
