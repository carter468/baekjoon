# 정복자
# Gold 3, MST

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