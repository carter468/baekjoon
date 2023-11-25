# 시루의 산책
# Gold 4, disjoint set

import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

n,m = map(int,input().split())
arr = [tuple(map(int,input().split())) for _ in range(n)]
p = tuple(map(int,input().split()))
r = tuple(map(int,input().split()))

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

c = [1]*n
d = r[0]**2
parent = list(range(n))
for i in range(n):
    x1,y1 = arr[i]
    k = find(i)
    for j in range(i+1,n):
        x2,y2 = arr[j]
        if (x1-x2)**2+(y1-y2)**2 <= d:
            j = find(j)
            if k != j:
                parent[j] = k
                c[k] += c[j]

marking = [0]*n
for i in range(m):
    x1,y1 = arr[p[i]-1]
    d = r[i+1]**2
    for j in range(n):
        x2,y2 = arr[j]
        if (x1-x2)**2+(y1-y2)**2 <= d:
            marking[j] = 1

result = set()
for i in range(n):
    if marking[i] == 0:
        result.add(find(i))

print(sum([c[i] for i in result]))