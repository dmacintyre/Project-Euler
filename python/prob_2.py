"""
prob_2.py

Description: 

Donald MacIntyre - djm4912
"""

def genFibNumSeq():
    s = [1,2]
    i = 2
    while True:
        s.append(s[i-2] + s[i-1])
        i += 1
        if s[i-1] >= 4000000 :
            break
    return s

def main() :
    lst = genFibNumSeq()
    sum = 0
    for i in lst :
        if i % 2 == 0:
           sum += i
    print(sum)


if __name__ == "__main__":
    main()
