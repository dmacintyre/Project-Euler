"""
prob_104.py

Description: 

Donald MacIntyre - djm4912
"""

import math
import decimal

def isNinePandigit(n):
    l = []
    for i in n:
        if i == '0':
            return False
        l.append(i)
    sl = set(l)
    if len(sl) != 9:
        return False
    ssl = sorted(sl)
    for i in range(1,10):
        if int(ssl[i-1]) != i:
            return False
    return True

def fib(n):
    phi = decimal.Decimal(1+math.sqrt(5))/2
    pn = phi**n
    p = ((-1)**n)/pn
    pt = pn-p
    return int(pt/decimal.Decimal(math.sqrt(5)))
        
def main() :
    f1 = 1
    f2 = 1
    i = 2
    while True:
            i += 1
            f = (f1 + f2) % 100000000000
            f1 = f2
            f2 = f
            pf2 = str(f2)
            if isNinePandigit(pf2[-9:]):
                n = str(fib(i))
                if isNinePandigit(str(n[:9])):
                    break
    print(i)
        
    
if __name__ == "__main__":
    main()
