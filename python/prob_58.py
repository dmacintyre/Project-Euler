"""
prob_58.py

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

def genDiagNum():
    l = []
    l.append(1)
    offset = 2
    i = 0
    count = 1
    prime = 0.0
    total = 0.0
    while True:
        for j in xrange(i,i+4):
            l.append(l[j] + offset)
            if isPrime(l[j] + offset):
                prime += 1
            total += 1
            
            if prime / total < 0.10 and j > 2:
                return int(count)
        count += 1
        i += 4 
        offset += 2

def main() :
    g = genDiagNum()
    print((g*2)-1)
    
if __name__ == "__main__":
    main()
