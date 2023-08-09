# 해밍 수열
# Gold 5, math, priority queue

import heapq

a,b,c,n = map(int,input().split())
q = [a,b,c]
heapq.heapify(q)
visit = {a,b,c}
for i in range(n):
    x = heapq.heappop(q)
    for j in (a,b,c):
        if x*j not in visit:
            heapq.heappush(q,x*j)
            visit.add(x*j)
print(x)