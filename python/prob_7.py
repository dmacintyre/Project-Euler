"""
prob_7.py

Description: 

Donald MacIntyre - djm4912
"""

def isPrime(n):
    for i in range(2,n):
        if (n % i == 0):
            return False
    return True

def main() :
    l=[]
    count = 2
    while(len(l) != 10001):
        if isPrime(count):
            l.append(count)
        count += 1
    print(l[10000])
    
if __name__ == "__main__":
    main()
