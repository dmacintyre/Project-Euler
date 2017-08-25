"""
prob_48.py

Description: 

Donald MacIntyre - djm4912
"""

def main() :
    last_ten = 0
    for i in range(1,1000):
        last_ten += i**i
        last_ten = last_ten % 10000000000
    print(last_ten)
    

if __name__ == "__main__":
    main()
