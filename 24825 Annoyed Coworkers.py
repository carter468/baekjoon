# Annoyed Coworkers
# Gold 5, priority queue

import heapq,sys

h,c = map(int,input().split())
result = 0
q = []
for _ in range(c):
    a,d = map(int,sys.stdin.readline().split())
    result = max(result,a)
    heapq.heappush(q,(a+d,d))

for _ in range(h):
    a,d = heapq.heappop(q)
    result = max(result,a)
    heapq.heappush(q,(a+d,d))
print(result)