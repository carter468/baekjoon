# 선수과목
# Gold 5, 위상정렬, 그래프이론

# import sys
# input = sys.stdin.readline

# n,m = map(int,input().split())
# graph = [[] for _ in range(n+1)]
# for _ in range(m):
#     a,b = map(int,input().split())
#     graph[a].append(b)

# depth = [1]*(n+1)
# for i in range(1,n+1):
#     for j in graph[i]:
#         depth[j] = max(depth[j],depth[i]+1)
# print(*depth[1:])

from collections import deque
import sys
input = sys.stdin.readline
n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
indegree = [0]*(n+1)
for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    indegree[b] += 1

depth = [1]*(n+1)
q = deque()
for i in range(1,n+1):
    if indegree[i]==0:
        q.append((i,1))
while q:
    node,count = q.popleft()
    for i in graph[node]:
        indegree[i] -= 1
        if indegree[i]==0:
            q.append((i,count+1))
            depth[i] = count+1
print(*depth[1:])