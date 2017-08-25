"""
prob_20.py

Description: 

Donald MacIntyre - djm4912
"""

def main() :
    r = 1
    for i in range(100,0,-1):
        r *= i
    a = str(r)
    s = 0
    for i in a:
        s += int(i)
    print(s)

if __name__ == "__main__":
    main()
