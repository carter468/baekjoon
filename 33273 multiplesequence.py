# multiple sequence
# Gold 2, greedy, topological sorting, DP

from collections import deque
import sys
input = sys.stdin.readline

N,M = map(int,input().split())
arr = sorted([tuple(map(int,input().split())) for _ in range(M)])

graph = [[] for _ in range(M)]
indegree = [0]*M
for i in range(M):
    for j in range(i+1,M):
        if arr[j][0]%arr[i][0] == 0:
            graph[j].append(i)
            indegree[i] += 1

order = []
q = deque([i for i in range(M) if indegree[i] == 0])
root = list(q)
while q:
    x = q.popleft()
    order.append(x)
    for nx in graph[x]:
        indegree[nx] -= 1
        if indegree[nx] == 0:
            q.append(nx)

dp = [[-1]*M for _ in range(M)]
for i in range(M):
    dp[i][i] = 0
for x in order:
    for nx in graph[x]:
        for s in range(M):
            if dp[s][x] != -1:  
                dp[s][nx] = max(dp[s][nx],dp[s][x]+1)

result = -1
for x in root:
    q = [(x,N,0)]
    while q:
        x,count,score = q.pop()
        c = arr[x][1]
        if c >= count:
            result = max(result,score+arr[x][0]*count)
            continue
        count -= c
        score += arr[x][0]*c
        for nx in graph[x]:
            if dp[x][nx] == 1:
                q.append((nx,count,score))
print(result)