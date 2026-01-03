# 급식 뭐 먹지
# Gold 4, priority queue

import sys,heapq
input = sys.stdin.readline

N,M = map(int,input().split())
A = sorted([tuple(map(int,input().split())) for _ in range(N)])

count = 0
heap = []
for a,b in A:
    heapq.heappush(heap,-b)
    while heap and -heap[0] > M-a:
        heapq.heappop(heap)
    count = max(count,len(heap))
print(count)