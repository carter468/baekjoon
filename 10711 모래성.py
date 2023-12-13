# 모래성
# Gold 2, BFS

from collections import deque

h,w = map(int,input().split())
arr = [list(input()) for _ in range(h)]

q = deque()
for i in range(h):
    for j in range(w):
        if arr[i][j] == '.':
            arr[i][j] = 0
            q.append((i,j))
        else:
            arr[i][j] = int(arr[i][j])

result = -1
while q:
    result += 1
    for _ in range(len(q)):
        x,y = q.popleft()
        for dx in (-1,0,1):
            for dy in (-1,0,1):
                if (dx,dy) == (0,0): continue
                nx,ny = x+dx,y+dy
                if 0 <= nx < h and 0 <= ny < w and arr[nx][ny] > 0:
                    arr[nx][ny] -= 1
                    if arr[nx][ny] == 0:
                        q.append((nx,ny))
print(result)