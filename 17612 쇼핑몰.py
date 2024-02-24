# 쇼핑몰
# Gold 2, priority queue

import sys,heapq
input = sys.stdin.readline

n,k = map(int,input().split())

empty = list(range(k))
heapq.heapify(empty)
result,r,t = 0,1,0
q = []
for _ in range(n):
    id,w = map(int,input().split())
    if empty:
        e = heapq.heappop(empty)
        heapq.heappush(q,(t+w,-e,id))
    else:
        t,e,i = heapq.heappop(q)
        result += r*i
        r += 1
        heapq.heappush(empty,-e)
        while q and q[0][0] == t:
            t,e,i = heapq.heappop(q)
            result += r*i
            r += 1
            heapq.heappush(empty,-e)
        e = heapq.heappop(empty)
        heapq.heappush(q,(t+w,-e,id))
while q:
    result += heapq.heappop(q)[2]*r
    r += 1
print(result)