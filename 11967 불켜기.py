# 불 켜기
# Gold 2, 너비 우선 탐색

from collections import defaultdict,deque
import sys
input = sys.stdin.readline
dx = [1,-1,0,0]
dy = [0,0,1,-1]

N,M = map(int,input().split())
switch = defaultdict(list)
for _ in range(M):
    x,y,a,b = map(int,input().split())
    switch[(x,y)].append((a,b))

light = [[0 for _ in range(N+1)] for _ in range(N+1)]
visit = [[0 for _ in range(N+1)] for _ in range(N+1)]
light[1][1] = 1
visit[1][1] = 1
count = 1
q = deque([(1,1)])
while q:
    x,y = q.popleft()

    for a,b in switch[(x,y)]:   # 현재 방의 스위치 켜기
        if light[a][b] == 0:
            count += 1
            light[a][b] = 1
            for i in range(4):
                nx = a+dx[i]
                ny = b+dy[i]
                if nx<1 or nx>N or ny<1 or ny>N:
                    continue
                if visit[nx][ny] == 1:  # 스위치 켠 방으로 갈 수 있다면 탐색
                    q.append((nx,ny))

    for i in range(4):      # 이동
        nx = x+dx[i]
        ny = y+dy[i]
        if nx<1 or nx>N or ny<1 or ny>N:
            continue
        if visit[nx][ny]==0 and light[nx][ny]==1:   # 미방문, 불켜짐
            q.append((nx,ny))
            visit[nx][ny] = 1

print(count)