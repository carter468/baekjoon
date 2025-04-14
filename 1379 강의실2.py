# 강의실 2
# Gold 3, priority queue, greedy

import sys,heapq
input = sys.stdin.readline

N = int(input())
arr = sorted([tuple(map(int,input().split())) for _ in range(N)],key=lambda x:x[1])

q = []
room = list(range(1,N+1))
heapq.heapify(room)
result = [0]*(N+1)
for idx,start,end in arr:
    while q and q[0][0] <= start:
        heapq.heappush(room,heapq.heappop(q)[1])
    r = heapq.heappop(room)
    result[idx] = r
    heapq.heappush(q,(end,r))

print(max(result[1:]),*result[1:],sep='\n')