# Frogs
# Gold 2, sweeping, priority queue

import sys,heapq
input = sys.stdin.readline

for _ in range(int(input())):
    N = int(input())

    start = [[] for _ in range(N)]
    for i in range(N):
        r,s = map(int,input().split())
        start[max(0,i-r)].append((s,i+r))

    result = 0
    heap = []
    for i in range(N):
        for s,r in start[i]:
            heapq.heappush(heap,(-s,r))
        arr = []
        while heap:
            s,r = heapq.heappop(heap)
            if r >= i:
                arr.append((-s,r))
            if len(arr) == 3:
                result = max(result,sum([arr[i][0] for i in range(3)]))
                break
        for s,r in arr:
            heapq.heappush(heap,(-s,r))
    print(result)