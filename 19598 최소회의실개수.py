# 최소 회의실 개수
# Gold 5, priority_queue, sweeping

import sys, heapq
input = sys.stdin.readline

arr = sorted([list(map(int,input().split())) for _ in range(int(input()))])

result, count = 0, 0
heap = []
for s, e in arr:
    while heap and heap[0] <= s:
        heapq.heappop(heap)
        count -= 1
    heapq.heappush(heap,e)
    count += 1
    result = max(result,count)
    
print(result)