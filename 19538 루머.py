# 루머
# Gold 4, BFS

from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]
C = [0]*(n+1)
count = [0]*(n+1)
for i in range(n):
    arr = tuple(map(int,input().split()))
    for a in arr[:-1]:
        graph[i+1].append(a)
        C[i+1] = len(arr)-1

visited = [-1]*(n+1)
q = deque()
input()
for a in map(int,input().split()):
    visited[a] = 0
    q.append(a)

while q:
    x = q.popleft()
    for nx in graph[x]:
        count[nx] += 1
        if visited[nx] == -1 and count[nx]*2 >= C[nx]:
            visited[nx] = visited[x]+1
            q.append(nx)

print(*visited[1:])
