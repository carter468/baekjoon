# 이모티콘
# Gold 4, BFS

from collections import deque

M = 1001
s = int(input())

visited = [[-1]*M for _ in range(M)]
visited[1][0] = 0
q = deque([(1,0)])
while q:
    a,b = q.popleft()
    if a == s:
        print(visited[a][b])
        break
    c = visited[a][b]
    if visited[a][a] == -1:
        visited[a][a] = c+1
        q.append((a,a))
    if a+b < M and visited[a+b][b] == -1:
        visited[a+b][b] = c+1
        q.append((a+b,b))
    if a-1 >= 0 and visited[a-1][b] == -1:
        visited[a-1][b] = c+1
        q.append((a-1,b))