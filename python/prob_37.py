"""
prob_37.py

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

def main() :
    i = 11
    ele = 0
    psum = 0
    while True:
        f1 = True
        f2 = False
        for j in range(len(str(i))):
            if j > 0:
                f1 = isPrime(int(str(i)[:-j]))
            f2 = isPrime(int(str(i)[j:]))
            if (f1 == False) or (f2 == False):
                break
        if f1 == True and f2 == True:
            ele += 1
            psum += i
        if ele == 11:
            break
        i += 2
    print(psum)
        
if __name__ == "__main__":
    st = time.clock()
    main()
    print(time.clock()-st)
