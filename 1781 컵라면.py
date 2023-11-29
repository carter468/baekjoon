# 컵라면
# Gold 2, greedy, priority queue

import sys,heapq
input = sys.stdin.readline

q = []
for limit,reward in sorted([tuple(map(int,input().split())) for _ in range(int(input()))]):
    heapq.heappush(q,reward)
    if limit < len(q):
        heapq.heappop(q)
print(sum(q))