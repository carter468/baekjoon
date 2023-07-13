# 빠른 오름차순 숫자 탐색
# Gold 5, BFS

from collections import deque

def bfs(start,end):
    q = deque([start])
    visit = [[0]*5 for _ in range(5)]
    visit[start[0]][start[1]] = 1
    while q:
        x,y = q.popleft()
        if (x,y)==end:
            return visit[x][y]-1
        for nx,ny in (x+1,y),(x-1,y),(x,y+1),(x,y-1):
            if 0<=nx<5 and 0<=ny<5 and visit[nx][ny]==0 and arr[nx][ny]!=-1:
                q.append((nx,ny))
                visit[nx][ny] = visit[x][y]+1
    return -1

arr = [tuple(map(int,input().split())) for _ in range(5)]
num = [0]*7
num[0] = tuple(map(int,input().split()))
for i in range(5):
    for j in range(5):
        if arr[i][j]>0:
            num[arr[i][j]] = (i,j)

result = 0
for i in range(6):
    a = bfs(num[i],num[i+1])
    if a==-1:
        print(a)
        break
    result += a
else:
    print(result)