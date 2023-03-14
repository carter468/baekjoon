# 정복자
# Gold 3, MST

# kruskal

import sys
input = sys.stdin.readline

def find(x):
    if parent[x]!=x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a,b):
    a,b=find(a),find(b)
    if a>b:
        parent[a] = b
    else:
        parent[b] = a

n,m,t = map(int,input().split())
graph = sorted([tuple(map(int,input().split())) for _ in range(m)],key=lambda x:x[2])
parent = list(range(n+1))

result = t*(n-2)*(n-1)//2
for a,b,cost in graph:
    if find(a)!=find(b):
        union(a,b)
        result += cost

print(result)

# prim

# import sys,heapq
# input = sys.stdin.readline

# n,m,t = map(int,input().split())
# graph = [[] for _ in range(n+1)]
# for _ in range(m):
#     a,b,c = map(int,input().split())
#     graph[a].append((c,b))
#     graph[b].append((c,a))

# visit = [0]*(n+1)
# q = [(0,1)]
# result = t*(n-2)*(n-1)//2
# while q:
#     c,n = heapq.heappop(q)
#     if visit[n]: continue
#     visit[n] = 1
#     result += c
#     for nc,nn in graph[n]:
#         heapq.heappush(q,(nc,nn))

# print(result)