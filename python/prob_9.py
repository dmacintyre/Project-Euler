"""
prob_9.py

Description: 

Donald MacIntyre - djm4912
"""

def equals1000(a,b,c):
    return a+b+c == 1000
        
def isTriple(a,b,c):
    if a < b and b < c and (a*a)+(b*b)==(c*c):
        return True
    return False

def find():        
    for a in range(0,1000):
        for b in range(0,1000):
            for c in range(0,1000):
                if equals1000(a,b,c) and isTriple(a,b,c):
                    return a,b,c
def main() :
    a,b,c = find()
    print(a*b*c)
    
if __name__ == "__main__":
    main()
