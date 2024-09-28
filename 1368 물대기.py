# 물대기
# Gold 2, MST

import heapq

def find(x):
    if root[x] != x:
        root[x] = find(root[x])
    return root[x]

n = int(input())
w = [int(input()) for _ in range(n)]
arr = [tuple(map(int,input().split())) for _ in range(n)]

edge = []
for i in range(n):
    heapq.heappush(edge,(w[i],i,n))
    for j in range(i+1,n):
        heapq.heappush(edge,(arr[i][j],i,j))

root = list(range(n+1))
result = 0
count = 0
while count < n:
    a,b,c = heapq.heappop(edge)
    b,c = find(b),find(c)
    if b != c:
        count += 1
        result += a
        root[b] = c
print(result)
