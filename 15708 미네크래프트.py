# 미네크래프트
# Platinum 5, priority queue, greedy

import heapq

N,T,P = map(int,input().split())
K = tuple(map(int,input().split()))

result = 0
count = 0
total = 0
heap = []
for i in range(N):
    if T-P*i <= 0: break
    
    total += K[i]
    count += 1
    heapq.heappush(heap,-K[i])

    while total > T-P*i:
        total += heapq.heappop(heap)
        count -= 1
    result = max(result,count)
print(result)