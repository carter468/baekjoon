# 강의실 배정
# Gold 5, 그리디

import sys,heapq
input = sys.stdin.readline

arr = sorted([tuple(map(int,input().split())) for _ in range(int(input()))])

result = 0
q = []
for s,e in arr:
    while q and q[0] <= s:
        heapq.heappop(q)
    heapq.heappush(q,e)
    result = max(result,len(q))

print(result)