# 허수아비
# Gold 3, greedy, priority queue

import heapq

_,P = map(int,input().split())

result = []
heap = []
t = 0
for a in map(int,input().split()):
    t += a
    heapq.heappush(heap,a)
    while t-heap[0] >= P:
        t -= heapq.heappop(heap)
    result.append(len(heap) if t >= P else -1)
print(*result)