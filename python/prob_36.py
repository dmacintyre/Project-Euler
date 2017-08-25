"""
prob_36.py

Description: 

Donald MacIntyre - djm4912
"""

def main() :
    s = 0
    for i in range(0,1000001):
        bini = bin(i)[2:]
        if (str(i) == str(i)[::-1]) and (bini == bini[::-1]) :
            s += i
    print(s)
            

if __name__ == "__main__":
    main()
