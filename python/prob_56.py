"""
prob_56.py

Description: 

Donald MacIntyre - djm4912
"""

def main() :
    l = []
    w = []
    for i in range(1,100):
        for j in range(1,100):
            l.append(i**j)
    
    for i in l:
        su = 0
        s = str(i)
        for j in s:
            su += int(j)
        w.append(su)
    print(max(w))
            

if __name__ == "__main__":
    main()
