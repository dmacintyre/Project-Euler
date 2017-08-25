"""
prob_31.py

Description: 

Donald MacIntyre - djm4912
"""

def main() :
    sol = 0
    for p200p in range(0,2):
        for p100p in range(0,3):
            for p50p in range(0,4):
                for p20p in range(0,11):
                    for p10p in range(0,21):
                        for p5p in range(0,41):
                            for p2p in range(0,101):
                                sol += 1
    print(sol)

if __name__ == "__main__":
    main()
