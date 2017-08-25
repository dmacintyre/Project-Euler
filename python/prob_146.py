"""
prob_146.py

Description: 

Donald MacIntyre - djm4912
"""

import math

def isPrime(n):
    s = math.sqrt(n)
    for i in range(2,n):
        if (n % i == 0):
            return False
        if i > s:
            break
    return True

def primeSequence(n):
    return isPrime((n**2)+1) and\
           isPrime((n**2)+3) and\
           isPrime((n**2)+7) and\
           isPrime((n**2)+9) and\
           isPrime((n**2)+13) and\
           isPrime((n**2)+27)
def main() :
    s = 0
    for i in range(1,1000001):
        if primeSequence(i):
            s += i
    print(s)


if __name__ == "__main__":
    main()
