# 민서의 응급 수술
# Gold 4, disjoint_set, tree

import sys
input = sys.stdin.readline

def find(x):
    if root[x] != x:
        root[x] = find(root[x])
    return root[x]

def union(a,b):
    a,b = find(a),find(b)
    if a > b:
        root[a] = b
    else:
        root[b] = a
    return a == b

n,m = map(int,input().split())

root = list(range(n+1))
result = -1
for _ in range(m):
    u,v = map(int,input().split())
    result += union(u,v)
for i in range(1, n+1):
    if root[i] == i:
        result += 1

print(result)