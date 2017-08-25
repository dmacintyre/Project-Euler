"""
prob_16.py

Description: 

Donald MacIntyre - djm4912
"""

def main() :
    n = 2 ** 1000
    i = str(n)
    s = 0
    for element in i:
        s += int(element)
    print(s)

if __name__ == "__main__":
    main()
