"""
prob3.py

Description: 

Donald MacIntyre - djm4912
"""

def calcPrimeFactors(n) :
    half = n / 4
    l = []
    i = 2 
    while True :
        if n % i == 0 :
          l.append(i)
        sum = 1
        for e in l :
            sum *= e
        i += 1
        if sum == n :
            return l

def main() :
    print(calcPrimeFactors(600851475143))

if __name__ == "__main__":
    main()
