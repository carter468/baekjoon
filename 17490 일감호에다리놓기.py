# 일감호에 다리 놓기
# Gold 3, MST, disjoint set

import sys,heapq
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def find(x):
    if root[x] != x:
        root[x] = find(root[x])
    return root[x]

n,m,k = map(int,input().split())
arr = tuple(map(int,input().split()))
b = [True]*(n+1)
for _ in range(m):
    i,j = map(int,input().split())
    i,j = i-1,j-1
    if i > j: i,j = j,i
    if (i,j) == (0,n-1): i,j = n-1,0
    b[i] = False

root = list(range(n))
for i in range(n):
    if b[i] == True:
        x = find(i)
        y = find((i+1)%n)
        if arr[x] <= arr[y]: x,y = y,x
        root[y] = x
q = []
for i in range(n):
    heapq.heappush(q,(arr[i],find(i)))

count = 0
c = [False]*(n+1)
if m == 1: m = 0
while count < m:
    x,y = heapq.heappop(q)
    y = find(y)
    if c[y] == True: continue
    k -= x
    c[y] = True
    count += 1
print('YES' if k >= 0 else 'NO')
