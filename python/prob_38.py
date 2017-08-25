"""
prob_38.py

Description: 

Donald MacIntyre - djm4912
"""

import itertools

def genPandigit():
    l = []
    t = []
    for i in xrange(1,10):
        c = i
        e = ""
        while c > 0:
            e += str(c)
            c -= 1
        l = list(itertools.permutations(e))
        for i in l:
            test = ""
            for j in i:
                test += j
            t.append(int(test))
    return t

def main() :
    p = genPandigit()
    p9 = []
    sol = []
    for i in p:
        if len(str(i)) == 9:
            p9.append(i)

    mval = max(p9)
    res = []
    for i in range(1,9999):
        s = ""
        n = 1
        while len(s) < 9:
            s += str(n*i)
            n += 1
            if len(s) == 9:
                res.append(s)
    for j in res:
        if int(j) in p9:
            sol.append(j)
    print(max(sol))
    
if __name__ == "__main__":
    main()
