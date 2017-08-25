"""
prob_22.py

Description: 

Donald MacIntyre - djm4912
"""

def calcLetterScore(c):
    return ord(c) - 64

def calcName(l):
    s = 0
    for i in l:
        s += calcLetterScore(i)
    return s

def main() :
    f = open("names.txt")
    for i in f:
        names = i.split(",")
    name = []
    for i in names:
        name.append(i[1:-1])
    name.sort()

    s = 0
    for j in xrange(len(name)):
        if j == 937 :
            print calcName(name[j])
        s += (j+1) * calcName(name[j])
    print(s)
    
if __name__ == "__main__":
    main()
