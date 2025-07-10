# 대동여지도
# Gold 3, MST

import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

def find(x):
    if root[x] != x:
        root[x] = find(root[x])
    return root[x]

N,M = map(int,input().split())
P = dict()
for i,p in enumerate(map(int,input().split())):
    P[p] = i
edge = sorted([tuple(map(int,input().split())) for _ in range(M)],key=lambda x:(x[2],P[x[3]]))

root = list(range(N+1))
result = [[0,0],[0,0],[0,0],0]

for u,v,w,k in edge:
    u,v = find(u),find(v)
    if u != v:
        root[u] = v
        result[3] += w
        result[k][0] += 1
        result[k][1] += w

print(result[3])
for i in range(3):
    print(*result[i])