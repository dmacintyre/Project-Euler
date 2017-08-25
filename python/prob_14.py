"""
prob_14.py

Description: 

Donald MacIntyre - djm4912
"""

def calculateNextCollatzNum(n):
    if n % 2 == 0:
        return n/2
    else :
        return 3*n+1

def calcTerms(n):
    count = 1
    while(n != 1):
        n = calculateNextCollatzNum(n)
        count += 1
    return count

def main() :
    max_len = 0
    current_len = 0
    leader = 0
    for i in xrange(1,1000001):
        current_len = calcTerms(i)
        if current_len > max_len:
            max_len = current_len
            leader = i
    print(leader)

if __name__ == "__main__":
    main()
