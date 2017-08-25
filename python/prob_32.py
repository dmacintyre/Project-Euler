"""
prob_32.py

Description: 

Donald MacIntyre - djm4912
"""

def fact(n):
    s = 1
    for i in xrange(n,0,-1):
        s *= i
    return s

def sumDigitF(n):
    s = 0
    while n > 0:
        d = n % 10
        n /= 10
        s += fact(d)
    return s
        
def main() :
    s = 0
    for i in xrange(3,2540160):
        if sumDigitF(i) == i:
            s += i
    print(s)
if __name__ == "__main__":
    main()
