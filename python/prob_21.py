"""
prob_21.py

Description: 

Donald MacIntyre - djm4912
"""

def calcDivisors(n):
    l = []
    for i in range(1,n):
        if n % i == 0:
            l.append(i)
    return l

def main() :
    s = 0
    for i in range(1,10001):
        d1 = calcDivisors(i)
        sd1 = sum(d1)        # amicable number must be this if it exists
        d2 = calcDivisors(sd1)
        sd2 = sum(d2)
        if sd2 == i and i != sd1:
            s += i
    print(s)
        
if __name__ == "__main__":
    main()
