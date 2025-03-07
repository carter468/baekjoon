# 개미의 이동
# Gold 3, ad hoc

import sys
input = sys.stdin.readline

L,T = map(int,input().split())
N = int(input())
ants = [input().split() for _ in range(N)]

T %= L*2
result = []
for i in range(N):
    x,d = ants[i]
    x = int(x)
    if d == 'D':
        x += T
        if x > L: x = abs(L*2-x)
    else:
        x -= T
        x = abs(x)
        if x > L: x = L*2-x
    result.append(x)

print(*sorted(result))