"""
prob_52.py

Description: 

Donald MacIntyre - djm4912
"""

def containSameDigit(n,m):
    sn = []
    sm = []
    for i in str(n):
        sn.append(i)
    for i in str(m):
        sm.append(i)
    ssn = sorted(set(sn))
    ssm = sorted(set(sm))
    return ssn == ssm

def main() :
    j = 1
    while True:
        for i in range(1,7):
            flag = containSameDigit(j,j*i)
            if flag == False:
                break
        if flag == True:
            break
        j += 1
    print(j)
    
if __name__ == "__main__":
    main()
