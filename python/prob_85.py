"""
prob_85.py

Description: 

Donald MacIntyre - djm4912
"""

import math

def countRect(l):
    s = 0
    for row in xrange(len(l)):
        for col in xrange(len(l[0])):
            for i in xrange(len(l)):
                for j in xrange(len(l[0])):
                    try:
                        l[row+i][col+j] = 0
                        s += 1
                    except IndexError :
                        pass
    return s

def main() :
    c = 0
    ans = 1
    for row in xrange(1,2000):
        for col in xrange(1,2000):
            l = [[0]*col]*row
            if math.fabs(countRect(l) - 2000000) < math.fabs(c - 2000000):
                c = countRect(l)
                ans = row * col
    print(ans)
                


if __name__ == "__main__":
    main()
