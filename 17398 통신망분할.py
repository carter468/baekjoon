# 통신망 분할
# Platinum 5, offline query, disjoint set

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def find(x):
    if root[x] != x:
        root[x] = find(root[x])
    return root[x]

N,M,Q = map(int,input().split())
edge = [tuple(map(int,input().split())) for _ in range(M)]
query = [int(input()) for _ in range(Q)]

query_set = set(query)
root = list(range(N+1))
count = [1]*(N+1)

for i in range(M):
    if i+1 not in query_set:
        x,y = edge[i]
        x,y = find(x),find(y)
        if x != y:
            root[x] = y
            count[y] += count[x]

result = 0
while query:
    x,y = edge[query.pop()-1]
    x,y = find(x),find(y)
    if x != y:
        result += count[x]*count[y]
        root[x] = y
        count[y] += count[x]
print(result)