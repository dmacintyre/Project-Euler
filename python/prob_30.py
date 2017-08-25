"""
prob_30.py

Description: 

Donald MacIntyre - djm4912
"""

def main() :
    s = 0
    for i in xrange(2,295245):
        l = str(i)
        single = 0
        for j in l:
            single += int(j) ** 5
        if single == i:
            s += i
    print(s)

if __name__ == "__main__":
    main()
