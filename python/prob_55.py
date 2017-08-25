"""
prob_55.py

Description: 

Donald MacIntyre - djm4912
"""

def reverseAndAdd(n):
    sn = str(n)
    rsn = sn[::-1]
    return n + int(rsn)

def isPal(n):
    return str(n) == str(n)[::-1]

def isLychrel(n):
    for i in xrange(50):
        n = reverseAndAdd(n)
        if isPal(n):
            return False
    return True
    
def main() :
    count = 0
    for i in xrange(1,10001):
        if isLychrel(i):
            count += 1
    print(count)
    
if __name__ == "__main__":
    main()
