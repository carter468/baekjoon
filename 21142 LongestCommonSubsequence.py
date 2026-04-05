# Longest Common Subsequence
# Gold 1, DP, DAG, topological sorting

from collections import deque
import sys
input = sys.stdin.readline

N,K = map(int,input().split())
pos = [[0]*K for _ in range(N)]
for i in range(N):
    for j,a in enumerate(input().strip()):
        pos[i][ord(a)-65] = j

graph = [[] for _ in range(K)]
indegree = [0]*K
for i in range(K):
    for j in range(K):
        for k in range(N):
            if pos[k][i] >= pos[k][j]: break
        else:
            graph[i].append(j)
            indegree[j] += 1

q = deque()
lcs = [0]*K
for i in range(K):
    if indegree[i] == 0:
        q.append(i)
        lcs[i] = 1

while q:
    x = q.popleft()
    for nx in graph[x]:
        indegree[nx] -= 1
        lcs[nx] = max(lcs[nx],lcs[x]+1)
        if indegree[nx] == 0:
            q.append(nx)
print(max(lcs))