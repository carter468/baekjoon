# 어려운 모든 정점 쌍 최단 거리
# Gold 4, disjoint set

import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

def find(x):
    if root[x] != x:
        root[x] = find(root[x])
    return root[x]

N,M,K = map(int,input().split())

root = list(range(N+1))
count = [1]*(N+1)
for i in range(M):
    u,v = map(int,input().split())
    if i+1 == K:
        a,b = u,v
    else:
        u,v = find(u),find(v)
        if u != v:
            root[u] = v
            count[v] += count[u]

a,b = find(a),find(b)
print(count[a]*count[b] if a != b else 0)