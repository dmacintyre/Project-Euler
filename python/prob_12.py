"""
prob_12.py

Description: 

Donald MacIntyre - djm4912
"""

import math

def main() :
    n = 1
    while(True):
        s = 0
        for i in xrange(1,n+1):
            s += i
        count = 0
        for j in xrange(1,s+1):
            a = math.sqrt(s)
            if j > a :
                count *= 2
                break
            if (s % j == 0):
                count += 1
        if count > 500:
            break
        n += 1
    print(s)
    
if __name__ == "__main__":
    main()
