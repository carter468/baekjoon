# 겹치는 선분
# Gold 4, 스위핑

import sys,heapq
input = sys.stdin.readline

arr = sorted([tuple(map(int,input().split())) for _ in range(int(input()))])
heap = [arr[0][1]]
result = 1
for s,e in arr[1:]:
    while heap and heap[0] <= s:
        heapq.heappop(heap)
    heapq.heappush(heap,e)
    result = max(result,len(heap))
print(result)