# 가희와 프로세스 1
# Gold 5, priority queue

import sys,heapq
input = sys.stdin.readline

t,n = map(int,input().split())
q = []
for _ in range(n):
    a,b,c = map(int,input().split())
    heapq.heappush(q,(-c,a,b))

for _ in range(t):
    c,a,b = heapq.heappop(q)
    print(a)
    if b > 1:
        heapq.heappush(q,(c+1,a,b-1))
    if not q: break
