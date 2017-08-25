"""
prob_42.py

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

def calcTriangle(m):
    l = []
    n = 1
    y = 0
    while( y < m):
        y = int(0.5*n*(n+1))
        l.append(y)
        n += 1
    return l

def main() :
    f = open("words.txt")
    words = []
    score = []
    count = 0
    for line in f:
        line = line.split(",")
    for i in line:
        words.append(i[1:-1])
    f.close()
    for i in words:
        score.append(calcName(i))
    c = calcTriangle(max(score))
    for i in score:
        if i in c:
            count += 1
    print(count)
            
            
    
    

if __name__ == "__main__":
    main()
