# 친구비
# Gold 4, 분리집합

import sys
input = sys.stdin.readline

def find(x):
    if root[x] != x:
        root[x] = find(root[x])
    return root[x]

def union(a,b):
    a,b = find(a),find(b)
    if cost[a] > cost[b]:
        root[a] = b
    else:
        root[b] = a

n,m,k = map(int,input().split())
cost = tuple(map(int,input().split()))
root = list(range(n))
for _ in range(m):
    v,w = map(int,input().split())
    union(v-1,w-1)

result = 0
for i in range(n):
    if find(i) == i:
        result += cost[i]

print('Oh no' if result > k else result)