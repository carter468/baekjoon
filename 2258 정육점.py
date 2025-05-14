# 정육점
# Gold 3, greedy

import sys
input = sys.stdin.readline
INF = sys.maxsize

N,M = map(int,input().split())
arr = sorted([tuple(map(int,input().split())) for _ in range(N)],key=lambda x:(x[1],-x[0]))

result = INF
t = 0
k = -1

for w,p in arr:
    t += w
    if p != k:
        k = p
        c = p
    else:
        c += p
    if t >= M: result = min(result,c)

print(result if result != INF else -1)