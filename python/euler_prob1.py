"""
euler_prob1.py

Description: 

Donald MacIntyre - djm4912
"""

def main() :
    sum = 0
    for i in range(1,1000):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
    print(sum)

if __name__ == "__main__":
    main()
