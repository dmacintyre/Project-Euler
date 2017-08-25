"""
prob_74.py

Description: 

Donald MacIntyre - djm4912
"""

def fact(n):
    s = 1
    for i in xrange(n,0,-1):
        s *= i
    return s

def genNextNum(n):
    a = 0
    while n > 0:
        i = n % 10
        a += fact(i)
        n = n / 10
    return a
        
def genChain(n):
    l = []
    l.append(n)
    while True:
        l.append(genNextNum(l[-1]))
        if len(set(l)) != len(l):
            return len(l)-1
    
def main() :
    s = 0
    for i in xrange(1,1000000):
        if genChain(i) == 60:
            s += 1
    print(s)
    
if __name__ == "__main__":
    main()
