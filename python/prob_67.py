"""
prob_67.py

Description: 

Donald MacIntyre - djm4912
"""

def main() :
    tree = []
    f = open("triangle.txt")
    for line in f:
        line = line.split()
        for j in range(0,100-len(line)):
            line.append(0)
        tree.append(line)
    f.close()

    for r in range(98,-1,-1):
        for c in range(99):
            if tree[r][c] != '0':
                left = int(tree[r][c]) + int(tree[r+1][c])
                right = int(tree[r][c]) + int(tree[r+1][c+1])
                if left > right:
                    tree[r][c] = left
                else:
                    tree[r][c] = right
    print(tree[0][0])

if __name__ == "__main__":
    main()
