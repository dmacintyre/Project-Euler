"""
prob_39.py

Description: 

Donald MacIntyre - djm4912
"""

import math

def genTriples(n):
    m = []
    for x in range(1,(n+1)):
        if x * 3 > n:
            break
        for y in range(x,(n+1)-x):
            z = int(math.sqrt((x*x)+(y*y)))
            if x + y + z == n and (x*x) + (y*y) == (z*z):
                m.append((x,y,z))
    return m

def main() :
    g = []
    for i in range(1,1001):
        g.append(genTriples(i))
    curr = 0
    m = 0
    count = 0
    i = 0
    for l in g:
        curr = len(l)
        if curr > m:
            m = curr
            i = count
        count += 1
    print(i+1)
    
   
    
if __name__ == "__main__":
    main()
