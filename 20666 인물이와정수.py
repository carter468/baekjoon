# 인물이와 정수
# Gold 3, greedy, prioirty queue

import sys,heapq
input = sys.stdin.readline

n,m = map(int,input().split())
c = [0]+list(map(int,input().split()))
penalty = [{} for _ in range(n+1)]
for _ in range(int(input())):
    a,b,t = map(int,input().split())
    penalty[a][b] = t
    c[b] += t

q = []
for i in range(1,n+1):
    heapq.heappush(q,(c[i],i))
result = 0
killed = [False]*(n+1)
while m > 0:
    d,i = heapq.heappop(q)
    if killed[i]: continue
    killed[i] = True
    m -= 1
    result = max(result,d)
    for x in penalty[i]:
        c[x] -= penalty[i][x]
        heapq.heappush(q,(c[x],x))
print(result)