# 숫자 놀이 3
# Gold 3, priority queue, ad hoc

import heapq

B,K = map(int,input().split())

v = set(range(1,B))
q = [(i,1) for i in range(1,B)]
heapq.heapify(q)
c = 0
result = []
while q:
    x,l = heapq.heappop(q)
    result.append(x)
    if len(result) == K: break
    for i in range(l,l*2+1):
        nx = x*i
        if nx <= 10**16 and nx not in v and B**(i-1) <= nx < B**i:
            v.add(nx)
            heapq.heappush(q,(nx,i))

print(*result,sep='\n')