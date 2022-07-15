# 토마토

# 모든 익은 토마토에 대해 bfs 를 이용하여 방문횟수를 구하면
# 가장 큰 수가 최소날짜가 된다.
from collections import deque
m,n,h = map(int,input().split())    # 가로 세로 높이

tomato = [[0 for _ in range(n)] for _ in range(h)] # 1:익은    0:익지않은      -1:비어있는

q = deque()      #queue
for i in range(h):
    for j in range(n):
        tomato[i][j] = list(map(int,input().split()))
        for k in range(m):
            if tomato[i][j][k] == 1:
                q.append([i,j,k])   # 익은 토마토를 큐에 넣는다
# 여섯개의 이동방향
dx = [1,-1,0,0,0,0]
dy = [0,0,1,-1,0,0]
dz = [0,0,0,0,1,-1]
day = 0        # 걸린 일수

while q:
    x,y,z = q.popleft()

    for i in range(6):
        a = x+dx[i]
        b = y+dy[i]
        c = z+dz[i]
        #   상자 안의 좌표이고      방문기록이 없고     안익은 토마토가 있을때
        if 0<=a<h and 0<=b<n and 0<=c<m and tomato[a][b][c] == 0:  
            tomato[a][b][c] = tomato[x][y][z] + 1
            q.append([a,b,c])
    
for i in tomato:
    for j in i:
        for k in j:
            if k == 0:          # 익지않은토마토가 존재할때
                print(-1)       # 불가능
                quit()
        day = max(day,max(j)-1)   # 0일차에 1이므로 걸린날짜는 1을 빼준다    
print(day)