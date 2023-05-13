# 파일 합치기 3
# Gold 4, 그리디, 우선순위큐

import sys, heapq
input = sys.stdin.readline

for _ in range(int(input())):
    k = int(input())
    heapq.heapify(size := list(map(int,input().split())))
    result = 0
    for _ in range(k-1):
        cost = heapq.heappop(size)+heapq.heappop(size)
        heapq.heappush(size,cost)
        result += cost
    print(result)