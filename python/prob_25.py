"""
prob_25.py

Description: 

Donald MacIntyre - djm4912
"""

def main() :
    l = [1,1]
    i = 0
    while True:
        l.append(l[i]+l[i+1])
        i += 1
        curr = str(l[-1])
        if len(curr) == 1000:
            break
    print(i+2)
        
if __name__ == "__main__":
    main()
