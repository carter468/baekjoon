# Secure Region
# Gold 2, bruteforcing

import sys
input = sys.stdin.readline

while True:
    X1,Y1,X2,Y2 = map(int,input().split())
    if X1 == Y1 == X2 == Y2 == 0: break

    N = int(input())
    mines = sorted([tuple(map(int,input().split())) for _ in range(N)]+[(X1,Y1),(X2,Y2)])

    N += 2
    result = (0,0)
    for i in range(N):
        x1 = mines[i][0]
        for j in range(i+1,N):
            x2 = mines[j][0]
            if x1 == x2: continue

            arr = sorted([Y1,Y2]+[mines[k][1] for k in range(i+1,j) if x1 < mines[k][0] < x2])
            p = x2-x1
            q = max([arr[k+1]-arr[k] for k in range(len(arr)-1)])
            if p > q: p,q = q,p
            if (p,q) > result: result = (p,q)

    print(*result)