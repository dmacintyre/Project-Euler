"""
prob_6.py

Description: 

Donald MacIntyre - djm4912
"""

def sumofsq(n):
    s = 0
    for i in range(1,n+1):
        s += i**2
    return s

def sqofsum(n):
    s = 0
    for i in range(1,n+1):
        s += i
    s = s * s
    return s

def main() :
    print(sqofsum(100)-sumofsq(100))
if __name__ == "__main__":
    main()
