"""
prob_23.py

Description: 

Donald MacIntyre - djm4912
"""

def divisors(n):
    l = []
    for i in range(1,(n//2)+1):
        if n % i == 0:
            l.append(i)
    return l

def status(n):
    # return -1 for deficient
    # return 0 for perfect
    # return 1 for abundant
    l = divisors(n);
    s = 0
    for i in l:
        s += i
    if s > n:
        return 1
    elif s == n:
        return 0
    return -1


def main() :
    num = []
    for i in range(1,28124):
        num.append(i)
    abundant_num = []
    for i in num:
        if status(i) == 1:
            abundant_num.append(i)
    print(len(abundant_num))
    s = sorted(abundant_num)
    two_sum = []
    for i in range(len(s)):
        for j in range(len(s)):
            if j > i:
                two_sum.append(s[i] + s[j])
    print(len(two_sum))
    s = set(two_sum)
    for i in s:
        if i < 28124:
            num.remove(i)
    sums = 0
    for i in num:
        sums += i
    print("Answer", sums)

if __name__ == "__main__":
    main()
