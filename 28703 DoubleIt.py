# Double It
# Gold 3, greedy, priority queue

import heapq

input()
arr = list(map(int,input().split()))

m = max(arr)
M = m
heapq.heapify(arr)
result = m-arr[0]
while arr[0] < M:
    x = heapq.heappop(arr)
    result = min(result,m-x)
    m = max(m,x*2)
    heapq.heappush(arr,x*2)

print(min(result,m-arr[0]))