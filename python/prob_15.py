"""
prob_15.py

Description: 

Donald MacIntyre - djm4912
"""

def main() :
    l = []
    l.append([1])
    l.append([1,1])
    for i in range(2,50):
        row = []
        row.append(1)
        step  = len(l[i-1])
        for j in range(1,step):
            row.append(l[i-1][j-1] + l[i-1][j])
        row.append(1)
        l.append(row)
    count = 0
    for i in l:
        if len(i) % 2 == 1:
            count += 1
        if count == 21:
            print(max(i))
            break
                    
    
    
if __name__ == "__main__":
    main()
