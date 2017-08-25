"""
prob_13.py

Description: 

Donald MacIntyre - djm4912
"""

def main() :
    a = 0
    f = open("prob_13.txt")
    for line in f:
        a += int(line)
    b = str(a)
    print(b[0:10])
    f.close()

if __name__ == "__main__":
    main()
