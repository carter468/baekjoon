# 숏코딩의 왕 브실이
# Gold 5, priority queue

import heapq

n,m = map(int,input().split())
arr = tuple(map(int,input().split()))

q = []
for i in range(m+1):
    heapq.heappush(q,(-arr[-1-i],m-i))
    
result = -10**5
for i in range(m+1):
    while q[0][1] < i:
        heapq.heappop(q)
    result = max(result,-q[0][0]-arr[i])

print(result)