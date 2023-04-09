# 소수의 곱
# Gold 1, 우선순위 큐

import heapq

_,n = map(int,input().split())
a = tuple(map(int,input().split()))

q = [1]
for _ in range(n+1):
    x = heapq.heappop(q)
    for i in a:
        heapq.heappush(q,x*i)
        if x%i == 0: break

print(x)