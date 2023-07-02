# 강의실
# Gold 5, greedy

import sys,heapq
input = sys.stdin.readline

arr = sorted([tuple(map(int,input().split())) for _ in range(int(input()))],key=lambda x:x[1])

result = 0
q = []
for _,a,b in arr:
    while q and q[0] <= a:
        heapq.heappop(q)
    heapq.heappush(q,b)
    result = max(result,len(q))

print(result)