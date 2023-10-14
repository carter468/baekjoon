# 연료 채우기
# Gold 2, greedy, priority queue

import sys,heapq
input = sys.stdin.readline

fuel = sorted([tuple(map(int,input().split())) for _ in range(int(input()))],reverse=True)
l,p = map(int,input().split())

count = 0
q = [0]
while q and p < l:
    while fuel and fuel[-1][0] <= p:
        heapq.heappush(q,-fuel.pop()[1])
    count += 1
    p += -heapq.heappop(q)

print(count if p >= l else -1)