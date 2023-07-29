# 특별한 서빙
# Gold 5, greedy, priority queue

import heapq

n,m = map(int,input().split())
q = []
result = 0
y = 0
for x in map(int,input().split()):
    heapq.heappush(q,-x)
    y += x
    while y >= m:
        y += 2*heapq.heappop(q)
        result += 1
print(result)