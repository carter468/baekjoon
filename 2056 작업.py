# 작업
# Gold 4, topological sorting, DP

from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
arr = [0]*(N+1)
graph = [[] for _ in range(N+1)]
indegree = [0]*(N+1)
for i in range(1,N+1):
    t,_,*num = map(int,input().split())
    arr[i] = t
    for j in num:
        graph[j].append(i)
        indegree[i] += 1

dp = [0]*(N+1)
q = deque()
for i in range(1,N+1):
    if indegree[i] == 0:
        q.append(i)

result = 0
while q:
    x = q.popleft()
    result = max(result,dp[x]+arr[x])
    for nx in graph[x]:
        dp[nx] = max(dp[nx],dp[x]+arr[x])
        indegree[nx] -= 1
        if indegree[nx] == 0: q.append(nx)
print(result)