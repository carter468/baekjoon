# 안정적인 네트워크
# Gold 3, 최소 스패닝 트리

import sys
input = sys.stdin.readline

def find(x):
    if root[x]!=x:
        root[x] = find(root[x])
    return root[x]

def union(a,b):
    a = find(a)
    b = find(b)
    if a<b:
        root[b] = a
    else:
        root[a] = b
    
n,m = map(int,input().split())
root = [i for i in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    union(a,b)

cost = []
input()
for i in range(2,n+1):
    arr = tuple(map(int,input().split()))
    for j in range(i+1,n+1):
        cost.append((arr[j-1],i,j))
cost.sort()

x,k = 0,0
connection = []
for c,i,j in cost:
    if find(i)!=find(j):
        connection.append((i,j))
        x += c
        k += 1
        union(i,j)

print(x,k)
for i in connection:
    print(*i)