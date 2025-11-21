# 슈퍼 학생
# Gold 5, greedy, priority queue

import sys,heapq
input = sys.stdin.readline

A,B,W,M = map(int,input().split())
F = sorted([int(input()) for _ in range(A)])
heap = []
for _ in range(W):
    heapq.heappush(heap,(-max(map(int,input().split())),B))

result = 0
while F:
    x = F.pop()
    a,b = heapq.heappop(heap)
    b += 1
    a = -max(-a,x)
    if b == M:
        result += (-a-1)*2
    else:
        heapq.heappush(heap,(a,b))
while heap:
    a,b = heapq.heappop(heap)
    result += (-a-1)*2
print(result)