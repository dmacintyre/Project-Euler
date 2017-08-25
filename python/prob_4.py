"""
prob_4.py

Description: 

Donald MacIntyre - djm4912
"""

def main() :
    l = []
    for i in range(100,1000):
        for j in range(100,1000):
            num = i * j
            if str(num) == str(num)[::-1]:
                l.append(num)
    print(max(l))
if __name__ == "__main__":
    main()
