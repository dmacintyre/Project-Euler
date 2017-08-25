"""
prob_92.py

Description: 

Donald MacIntyre - djm4912
"""

import time

start_time = time.clock()

def genNext(n):
    s = 0
    while n > 0:
        s += (n % 10) ** 2
        n //= 10
    return s

def genSeq(n):
    l = [n]
    while (l[-1] != 1) and l[-1] != 89:
        l.append(genNext(l[-1]))
    return l[-1]

def main() :
    count = 0
    for i in xrange(1,10000001):
        if genSeq(i) == 89:
            count += 1
    print(count)
            
if __name__ == "__main__":
    main()
    print(time.clock() - start_time) 
