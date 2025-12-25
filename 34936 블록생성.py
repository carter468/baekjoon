# 블록 생성
# Gold 5, priority queue

import sys,heapq
input = sys.stdin.readline

N,T,K = map(int,input().split())
heap = []
result = 0
for _ in range(N):
    q = tuple(map(int,input().split()))
    if q[0] == 1:
        t,f = q[1:]
        heapq.heappush(heap,(-f,t))
    else:
        t = q[1]
        c = 0
        while c < K and heap:
            a,b = heapq.heappop(heap)
            if t-b <= T:
                c += 1
                result -= a
print(result)