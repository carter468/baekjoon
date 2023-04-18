# 귀찮은 해강이
# Gold 5, 분리 집합

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

n,m = map(int,input().split())

root = list(range(n+1))
for _ in range(m):
    union(*map(int,input().split()))

arr = tuple(map(int,input().split()))
result = 0
for i in range(n-1):
    if find(arr[i]) != find(arr[i+1]):
        result += 1

print(result)