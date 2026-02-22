# 정사각형 따먹기
# Gold 2, ad hoc, constructive

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    W,H = map(int,input().split())
    result = []
    for i in range(W,1,-1):
        for j in range(H,1,-1):
            result.append((i,j))
    if (W+H)%2 == 0:
        for i in range(3-W%2,H+1,2):
            result.append((1,i))
        for i in range(3-W%2,W+1,2):
            result.append((i,1))
        if W%2 == 0: result.append((1,1))
    else:
        for i in range(2,H,2):
            result.append((1,i))
        for i in range(2,W,2):
            result.append((i,1))

    print(len(result))
    for r in result: print(*r)