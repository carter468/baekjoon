# Every? Only One's Marble
# Gold 1, implementation, simulation

import sys
input = sys.stdin.readline

n,m,W,G = map(int,input().split())
gk = [tuple(map(int,input().split())) for _ in range(G)]
gki = 0
arr = [0]*(4*n-4)
count = 0
for i in range(4*n-4):
    if i%(n-1) != 0:
        a = input().split()
        if a[0] == 'L':
            count += 1
            arr[i] = int(a[1])
        else:
            arr[i] = -1

x = 0
stop = 0
fund = 0
dice = [tuple(map(int,input().split())) for _ in range(int(input()))]
for a,b in dice:
    if stop > 0:
        if a == b: stop = 0
        else: stop -= 1
    else:
        x += a+b
        while x >= 4*n-4:
            m += W
            x -= 4*n-4
        if arr[x] == -1:
            c,d = gk[gki]
            gki = (gki+1)%G
            if c == 1:
                m += d
            elif c == 2:
                m -= d
                if m < 0:
                    print('LOSE')
                    break
            elif c == 3:
                m -= d
                fund += d
                if m < 0:
                    print('LOSE')
                    break
            else:
                x += d
                while x >= 4*n-4:
                    m += W
                    x -= 4*n-4
        if x == n-1:
            stop = 3
        elif x == n*2-2:
            m += fund
            fund = 0
        elif x == n*3-3:
            x = 0
            m += W
        elif arr[x] > 0:
            if m >= arr[x]:
                m -= arr[x]
                count -= 1
                arr[x] = 0
else:
    print('LOSE' if count > 0 else 'WIN')