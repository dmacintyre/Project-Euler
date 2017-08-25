"""
prob_45.py

Description: 

Donald MacIntyre - djm4912
"""

def genTriangle(n):
    return (n*(n+1))/2

def genPen(n):
    return ((n*((3*n)-1))/2)

def genHex(n):
    return n*((2*n)-1)

def main() :
    found = False
    currTriangle = 285
    latestP = 2
    latestH = 2
    while found == False:
        t = genTriangle(currTriangle)
        if t > genHex(latestH):
            latestH += 1
        if t > genPen(latestP):
            latestP += 1
        if genHex(latestH) == genPen(latestP) == t:
            found = True
        currTriangle += 1
    print(t)
        
if __name__ == "__main__":
    main()
