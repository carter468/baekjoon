# Fence Repair
# Gold 4, greedy, priority queue

import sys,heapq
input = sys.stdin.readline

arr = [int(input()) for _ in range(int(input()))]
heapq.heapify(arr)

result = 0
while len(arr) > 1:
    x = heapq.heappop(arr)+heapq.heappop(arr)
    result += x
    heapq.heappush(arr,x)
print(result)