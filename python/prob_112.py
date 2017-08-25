"""
prob_112.py

Description: 

Donald MacIntyre - djm4912
"""

def isIncreasing(n):
    s = str(n)
    for i in range(1,len(str(n))):
        if s[i] < s[i-1]:
            return False
    return True
        
def isDecreasing(n):
    s = str(n)
    for i in range(1,len(str(n))):
        if s[i] > s[i-1]:
            return False
    return True

def isBouncy(n):
    return not(isDecreasing(n) or isIncreasing(n)) 

def main() :
    bouncy = 0.0
    total = 0.0
    i = 1
    while True :
        if isBouncy(i):
            bouncy += 1
        total += 1
        if bouncy / total == 0.99:
            break
        i += 1
    print(i)

if __name__ == "__main__":
    main()
