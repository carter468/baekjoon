# 수영장 사장님
# Platinum 5, BFS

from collections import deque

n,m = map(int,input().split())
temp = [tuple(map(int,input().split())) for _ in range(n)]

arr = [[0]*(m+2) for _ in range(n+2)]
for i in range(n):
    for j in range(m):
        arr[i+1][j+1] = temp[i][j]

result = [[0]*(m+2) for _ in range(n+2)]
q = [deque() for _ in range(10001)]
visited = [[False]*(m+2) for _ in range(n+2)]
q[0].append((0,0))
for i in range(10001):
    while q[i]:
        x,y = q[i].popleft()
        if visited[x][y] == True: continue
        visited[x][y] = True
        result[x][y] = i
        for nx,ny in (x+1,y),(x-1,y),(x,y+1),(x,y-1):
            if 0 <= nx < n+2 and 0 <= ny < m+2:
                if visited[nx][ny] == True: continue
                if arr[nx][ny] <= i:
                    q[i].append((nx,ny))
                else:
                    q[arr[nx][ny]].append((nx,ny))

answer = 0
for i in range(1,n+1):
    for j in range(1,m+1):
        answer += result[i][j]-arr[i][j]
print(answer)