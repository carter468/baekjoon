# Puyo Puyo
# Gold 4, implementation, simulation, BFS

from collections import deque

arr = [list(input()) for _ in range(12)]

count = 0
while True:
    flag = False
    visited = [[False]*6 for _ in range(12)]
    for i in range(12):
        for j in range(6):
            if arr[i][j] != '.' and not visited[i][j]:
                q = deque([(i,j)])
                visited[i][j] = True
                temp = [(i,j)]
                while q:
                    x,y = q.popleft()
                    for nx,ny in (x+1,y),(x-1,y),(x,y+1),(x,y-1):
                        if 0 <= nx < 12 and 0 <= ny < 6 and not visited[nx][ny] and arr[nx][ny] == arr[i][j]:
                            visited[nx][ny] = True
                            q.append((nx,ny))
                            temp.append((nx,ny))
                if len(temp) >= 4:
                    flag = True
                    for x,y in temp:
                        arr[x][y] = '.'
    if not flag: break
    count += 1
    for j in range(6):
        a = -1
        for i in range(11,-1,-1):
            if arr[i][j] == '.':
                a = max(a,i)
            elif arr[i][j] != '.':
                if a != -1:
                    arr[a][j] = arr[i][j]
                    arr[i][j] = '.'
                    a -= 1
print(count)