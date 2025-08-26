# 언젠가 정렬이 될 수 있으면 좋겠네.
# Gold 1, topological sorting, priority queue

import heapq

def gcd(a,b):
    while b:
        a,b = b,a%b
    return a

N = int(input())
A = tuple(map(int,input().split()))

graph = [[] for _ in range(N)]
indegree = [0]*N
for i in range(N):
    for j in range(i+1,N):
        if gcd(A[i],A[j]) != 1:
            graph[i].append(j)
            indegree[j] += 1

q = []
for i in range(N):
    if indegree[i] == 0:
        heapq.heappush(q,(A[i],i))

result = []
while q:
    x,i = heapq.heappop(q)
    result.append(x)
    for ni in graph[i]:
        indegree[ni] -= 1
        if indegree[ni] == 0:
            heapq.heappush(q,(A[ni],ni))
print(*result)