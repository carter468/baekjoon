# 1과 5
# Gold 5, math, case work

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    N = input().strip()
    l = len(N)
    if N[-1] == '5': print(0,5)
    elif N[-2] == '5': print(l,5)
    else:
        c = 0
        five = 0
        for i in range(l):
            c += int(N[i])
            if N[i] == '5': five = i+1
        c %= 3
        if c == 0: print(0,3)
        elif c == 1: print(l,3)
        else: 
            if five: print(five,3)
            else:
                n = (l-2)//3
                if n%2 == 0: print(0,11)
                else: print(1,11)