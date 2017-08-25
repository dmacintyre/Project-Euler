"""
prob_28.py

Description: 

Donald MacIntyre - djm4912
"""

def genDiagNum(n):
    l = []
    l.append(1)
    offset = 2
    i = 0
    while len(l) < n:
        for j in xrange(i,i+4):
            l.append(l[j] + offset)
        i += 4 
        offset += 2
    return l

def main() :
    side = 1001
    l = (side * 2)-1
    g = genDiagNum(l)
    s = 0
    for i in g:
        s += i
    print(s)
    
if __name__ == "__main__":
    main()
