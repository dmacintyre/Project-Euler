"""
prob_34.py

Description: 

Donald MacIntyre - djm4912
"""

def fact(n):
    s = 1
    for i in range(n,0,-1):
        s *= i
    return s

def main() :
    total = 0
    for i in range(0,5):
        s = 0
        for a in str(i):
            s += fact(int(a))
        if s == i:
            total += s
    print(total)
if __name__ == "__main__":
    main()
