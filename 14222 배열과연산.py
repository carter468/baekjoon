# 배열과 연산
# Gold 5, greedy, priority queue

import heapq

n,k = map(int,input().split())
q = list(map(int,input().split()))

heapq.heapify(q)
i = 1
while i <= n:
    if q[0] != i:
        print(0)
        break
    heapq.heappop(q)
    while q and q[0] == i:
        heapq.heappush(q,heapq.heappop(q)+k)
    i += 1
else: print(1)