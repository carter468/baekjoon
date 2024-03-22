# 배수로
# Gold 3, disjoint set

import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

n,m = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

c = [1]*n
d = [0]*n
count = 0
for i in range(n):
    if b[i] > a[i]:
        count += 1
        d[i] = 1

parent = list(range(n))
for _ in range(m):
    q = tuple(map(int,input().split()))
    if q[0] == 2: print(count)
    else:
        x,y = find(q[1]-1),find(q[2]-1)
        if x == y: continue
        count -= c[x]*d[x]+c[y]*d[y]
        parent[y] = x
        a[x] += a[y]
        b[x] += b[y]
        c[x] += c[y]
        if b[x] > a[x]:
            d[x] = 1
            count += c[x]*d[x]
        else: d[x] = 0