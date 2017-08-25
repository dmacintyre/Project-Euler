"""
prob_43.py

Description: 

Donald MacIntyre - djm4912
"""

import itertools

def gen9DigitPandigit():
    l = []
    t = []
    for i in xrange(9,10):
        c = i
        e = ""
        while c >= 0:
            e += str(c)
            c -= 1
        l = list(itertools.permutations(e))
        for i in l:
            test = ""
            for j in i:
                test += j
            if test[0] != '0': 
                t.append((test))
    return t

def followRules(n):
    s = str(n)
    if int(s[1] + s[2]+ s[3]) % 2 != 0:
        #print("2")
        return False
    if int(s[2] + s[3]+ s[4]) % 3 != 0:
        #print("3")
        return False
    if int(s[3] + s[4]+ s[5]) % 5 != 0:
        #print("5")
        return False
    if int(s[4] + s[5]+ s[6]) % 7 != 0:
        #print("7")
        return False
    if int(s[5] + s[6]+ s[7]) % 11 != 0:
        #print("11")
        return False
    if int(s[6] + s[7]+ s[8]) % 13 != 0:
        #print("15")
        return False
    if int(s[7] + s[8]+ s[9]) % 17 != 0:
        #print("17")
        return False
    return True
            

def main() :
    s = 0
    p9 = gen9DigitPandigit()
    for i in p9:
        if followRules(i):
            s += int(i)
    print(s)
    
if __name__ == "__main__":
    main()
