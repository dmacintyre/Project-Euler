"""
prob_54.py

Description: 

Donald MacIntyre - djm4912
"""

def isSameSuit(cards):
    l = []
    for i in cards:
        l.append(i[1])
    return len(set(l)) == 1

def highCard(cards):
    return sorted(cards)[-1]

def isOnePair(cards):
    for i in cards:
        m = 0
        for j in range(len(cards)):
            if i[0] == cards[j][0]:
                m += 1
            if m == 2:
                return True
    return False


def main() :
    f = open("poker.txt",'r')
    for line in f:
        p1Cards = []
        p2Cards = []
        i = 0
        for card in line.strip().split():
            if i < 5:
                if card[0] == "T":
                    p1Cards.append((10,card[1]))
                elif card[0] == "J":
                    p1Cards.append((11,card[1]))
                elif card[0] == "Q":
                    p1Cards.append((12,card[1]))
                elif card[0] == "K":
                    p1Cards.append((13,card[1]))
                elif card[0] == "A":
                    p1Cards.append((14,card[1]))
                else :
                    p1Cards.append((int(card[0]),card[1]))    
            else :
                if card[0] == "T":
                    p2Cards.append((10,card[1]))
                elif card[0] == "J":
                    p2Cards.append((11,card[1]))
                elif card[0] == "Q":
                    p2Cards.append((12,card[1]))
                elif card[0] == "K":
                    p2Cards.append((13,card[1]))
                elif card[0] == "A":
                    p2Cards.append((14,card[1]))
                else :
                    p2Cards.append((int(card[0]),card[1]))
            i += 1
        if(isOnePair(p1Cards)):
            print(p1Cards)
        
    f.close()
    

if __name__ == "__main__":
    main()
