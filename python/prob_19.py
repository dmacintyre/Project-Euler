"""
prob_19.py

Description: 

Donald MacIntyre - djm4912
"""

import datetime

def daterange(sd, ed):
    for i in range(int ((ed - sd).days)):
        yield sd + datetime.timedelta(i)

def main() :
        sd = datetime.date(1901,1,1)
        ed = datetime.date(2000,12,31)
        s = 0
        for i in daterange(sd,ed):
            if i.weekday() == 6 and i.day == 1:
                s += 1
        print(s)

if __name__ == "__main__":
    main()
