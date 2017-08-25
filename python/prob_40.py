"""
prob_40.py

Description: 

Donald MacIntyre - djm4912
"""

def main() :
    l = []
    for i in range(1,1000001):
        for j in str(i):
            l.append(j)
    s = 1
    c = 1
    while c < 1000001:
        s *= int(l[c-1])
        c *= 10
    print(s)

if __name__ == "__main__":
    main()
