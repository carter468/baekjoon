# 치즈
# Gold 3, BFS

# 시간이 다른 정답자 코드의 10배 정도 된다.
# 매번 새로 BFS 돌리지 말고 없앤 치즈만 큐에 담아서 BFS 돌리면 빨라질것같다.
# visit도 초기화 할 필요없고 더 효율적일듯

from collections import deque
import sys
input = sys.stdin.readline

def bfs():
    visit = [[0]*m for _ in range(n)]
    visit[0][0] = 1
    q = deque([(0,0)])
    while q:
        x,y = q.popleft()
        for nx,ny in ((x+1,y),(x-1,y),(x,y+1),(x,y-1)):
            if nx < 0 or nx == n or ny < 0 or ny == m: continue
            if grid[nx][ny] == 0 and visit[nx][ny] == 0:
                q.append((nx,ny))
            visit[nx][ny] += 1

    flag = False
    for i in range(n):
        for j in range(m):
            if visit[i][j] > 1 and grid[i][j] == 1:
                grid[i][j] = 0
                flag = True
    return flag

n,m = map(int,input().split())
grid = [list(map(int,input().split())) for _ in range(n)]

count = 0
while bfs():
    count += 1

print(count)