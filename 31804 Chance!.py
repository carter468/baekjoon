# Chance!
# Gold 4, BFS

from collections import deque

a,b = map(int,input().split())

q = deque([(a,0)])
visited = [[-1]*2 for _ in range(b+1)]
visited[a][0] = 0
while q:
    x,y = q.popleft()
    if x == b:
        print(visited[b][y])
        break
    if x+1 <= b and visited[x+1][y] == -1:
        visited[x+1][y] = visited[x][y]+1
        q.append((x+1,y))
    if x*2 <= b and visited[x*2][y] == -1:
        visited[x*2][y] = visited[x][y]+1
        q.append((x*2,y))
    if y == 0 and x*10 <= b and visited[x*10][1] == -1:
        visited[x*10][1] = visited[x][y]+1
        q.append((x*10,1))