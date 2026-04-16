# 달력 놀이
# Gold 2, game theory, DP

import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

lim1 = [0,31,28,31,30,31,30,31,31,30,31,30,31]
lim2 = [0,31,29,31,30,31,30,31,31,30,31,30,31]

def solve(y,m,d):
    x = (y,m,d)
    if x in win: return win[x]

    win[x] = False
    # 다음날
    ny,nm,nd = y,m,d
    if (y%4 == 0 and y%100 != 0) or y%400 == 0:
        l = lim2[m]
    else:
        l = lim1[m]
    if d == l:
        nd = 1
        nm += 1
        if nm == 13:
            nm = 1
            ny += 1
    else: nd += 1
    win[x] |= not solve(ny,nm,nd)

    # 다음달
    m += 1
    if m == 13:
        m = 1
        y += 1
    elif (y%4 == 0 and y%100 != 0) or y%400 == 0:
        if d > lim2[m]: return win[x]
    elif d > lim1[m]: return win[x]
    if (y,m,d) <= (2001,11,4): win[x] |= not solve(y,m,d)

    return win[x]

win = {(2001,11,4):False}
solve(1900,1,1)

for _ in range(int(input())):
    print(['NO','YES'][win[tuple(map(int,input().split()))]])