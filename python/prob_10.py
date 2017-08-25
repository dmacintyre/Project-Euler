"""
prob_10.py

Description: 

Donald MacIntyre - djm4912
"""

import math

def isPrime(n):
    s = math.sqrt(n)
    for i in xrange(3,n):
        if (n % i == 0):
            return False
        if i > s:
            break
    return True

def main() :
    s = 2
    for i in xrange(3,2000001,2):
        if isPrime(i) :
            s += i
    print(s)
        
        
        
    
if __name__ == "__main__":
    main()
