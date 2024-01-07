# 게리맨더링
# Platinum 4, greedy

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    input()

    c,s = 0,0
    for a in map(int,input().split()):
        if a > 0:
            if s <= 0 and s+a > 0:
                s += a
            else:
                if s < 0: c -= 1
                else: c += 1
                s = a
        elif a < 0:
            if s > 0 and s+a <= 0:
                c += 1
                s = a
            else:
                s += a
    if s > 0: c += 1
    elif s < 0: c -= 1

    print('YES' if c > 0 else 'NO')