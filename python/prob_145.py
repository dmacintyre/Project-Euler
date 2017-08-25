"""
prob_145.py

Description: 

Donald MacIntyre - djm4912
"""

import time

def reverseN(n):
    a = str(n)
    ra = a[::-1]
    return int(ra)

def containsAllOddDigits(n):
    for i in str(n):
        if (int(i) % 2) == 0:
            return False
    return True

def main() :
    st = time.clock()
    count = 0
    for i in range(1,(10**9)+1):
        if i % 10 != 0:
            revi = reverseN(i)
            if containsAllOddDigits(revi + i) :
                count += 1
    print(count)
    print(time.clock()-st)
    
if __name__ == "__main__":
    main()
