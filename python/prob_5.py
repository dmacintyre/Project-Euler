"""
prob_5.py

Description: 

Donald MacIntyre - djm4912
"""

def main() :
    i = 2520
    while(True):
        flag = True
        for ii in range(20,2,-1):
            if (i % ii != 0):
                i += 1
                flag = False
        if flag == True:
            break
    print(i)
        

if __name__ == "__main__":
    main()
