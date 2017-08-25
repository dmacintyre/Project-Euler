"""
prob_29.py

Description: 

Donald MacIntyre - djm4912
"""

def main() :
    l = []
    for i in range(2,101):
        for j in range(2,101):
          print(j)
          print(char(j))
          l.append(i**j)
    setl = set(l)
    print(len(setl))

if __name__ == "__main__":
    main()
