# 화학 실험
# Gold 5, greedy, priority queue

import heapq

N,K = map(int,input().split())
C = tuple(map(int,input().split()))

heap = []
for i in range(K):
    heap.append((-C[i],i+1))
heapq.heapify(heap)

result = []
prev = None
for _ in range(N):
    if not heap:
        print(-1)
        break

    c,i = heapq.heappop(heap)
    result.append(i)

    if prev:
        heapq.heappush(heap,prev)
    if c+1 < 0:
        prev = (c+1,i)
    else:
        prev = None
else: print(*result)