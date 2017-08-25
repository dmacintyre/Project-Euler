"""
prob_59.py

Description: 

Donald MacIntyre - djm4912
"""

def main() :
    l = []
    f = open("cipher1.txt")
    for x in range(97,122):   
        for y in range(97,122):
            for z in range(97,122):
                l.append((x,y,z))
    for line in f:
        num = line.split(',')
    print(num(0)
    f.close()

if __name__ == "__main__":
    main()
