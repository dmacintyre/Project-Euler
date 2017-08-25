"""
prob_35.py

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

def shift(s):
    return s[1:]+s[0]

def main() :
    l = []
    for i in xrange(2,1000001):
        if isPrime(i):
            l.append(i)
    r = []
    for e in l:
        test = True
        n = e
        for a in str(e):
            n = shift(str(n))
            if isPrime(int(n)) == False:
                test = False
        if test == True:
            r.append(e)
                
                
    print((len(r)))
        
if __name__ == "__main__":
    main()
