# 아직은 어색해
# Gold 4, greedy

import sys
input = sys.stdin.readline

N,M = map(int,input().split())
arr = [tuple(map(int,input().split())) for _ in range(M)]
idx = int(input())-1

dist = [sys.maxsize]*M
result = []
for i in range(N):
    result.append(idx+1)
    x1,y1 = arr[idx]
    maxv,idx = -1,0
    for j in range(M):
        x2,y2 = arr[j]
        dist[j] = min(dist[j],(x1-x2)**2+(y1-y2)**2)
        if dist[j] > maxv:
            maxv,idx = dist[j],j
print(*result,sep='\n')