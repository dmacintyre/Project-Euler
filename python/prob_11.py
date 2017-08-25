"""
prob_11.py

Description: 

Donald MacIntyre - djm4912
"""

def checkRow(b):
    l = []
    for row in b:
        for c in range(20):
            try :
                l.append(row[c] * row[c+1] * row[c+2] * row[c+3])
            except IndexError:
                pass
    return l

def checkCol(b):
    l = []
    for r in range(20):
        for c in range(20):
            try:
                l.append(b[r][c] * b[r+1][c] * b[r+2][c] * b[r+3][c])
            except IndexError :
                pass
    return l

def checkDiag(b):
    l = []
    for r in range(20):
        for c in range(20):
            try:
                l.append(b[r][c] * b[r+1][c+1] * b[r+2][c+2] * b[r+3][c+3])
                if r -3 >= 0:
                    l.append(b[r][c] * b[r-1][c+1] * b[r-2][c+2] * b[r-3][c+3])
            except IndexError :
                pass
    return l

def main() :
    f = open("prob_11.txt")
    board = []
    r = 0
    c = 0
    for line in f:
        line = line.strip().split()
        c = 0
        row = []
        for a in line:
            row.append(int(a))
        board.append(row)
    f.close()
    r = max(checkRow(board))
    c = max(checkCol(board))
    d = max(checkDiag(board))
    print(r,c,d)

if __name__ == "__main__":
    main()
