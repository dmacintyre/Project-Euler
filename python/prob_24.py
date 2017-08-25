"""
prob_24.py

Description: 

Donald MacIntyre - djm4912
"""

import itertools

def main() :
    l = list(itertools.permutations("0123456789"))
    t = []
    for i in l:
        s = ""
        for j in i:
            s += j
        t.append(s)
    print(t[1000000-1])
    
if __name__ == "__main__":
    main()
