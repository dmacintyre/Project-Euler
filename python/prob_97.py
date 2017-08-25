"""
prob_97.py

Description: 

Donald MacIntyre - djm4912
"""

def main() :
    s = 1
    for i in range(7830457):
        s *= 2
        s = s % 10000000000
    s *= 28433
    s = s % 10000000000
    print(s+1)

if __name__ == "__main__":
    main()
