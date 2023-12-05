# 가희와 여행가요
# Gold 4, MST

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n,q = map(int,input().split())
edge = sorted([tuple(map(int,input().split())) for _ in range(q)],key=lambda x:(x[2],x[3]))

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

parent = list(range(n+1))
result = [0,0]
for x,y,c,t in edge:
    x,y = find(x),find(y)
    if x != y:
        parent[x] = y
        result[1] += c
        result[0] = max(result[0],t)

count = 0
for i in range(1,n+1):
    if i == find(i): count += 1

if count == 1: print(*result)
else: print(-1)