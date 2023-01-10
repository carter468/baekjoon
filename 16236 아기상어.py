# 아기 상어
# Gold 3, 너비 우선 탐색, 구현

from collections import deque
import sys
input = sys.stdin.readline

def find_fish(x,y):
    q = deque([(x,y)])
    distance = [[-1 for _ in range(N)] for _ in range(N)]
    distance[x][y] = 0
    option = [10000,[]]     # 최단거리, 먹이 후보
    while q:
        cx,cy = q.popleft()
        for i in range(4):
            nx = cx+dx[i]
            ny = cy+dy[i]
            if nx>=N or nx<0 or ny>=N or ny<0 or table[nx][ny]>size or distance[nx][ny] != -1:
                continue
            if 0<table[nx][ny]<size:    # 먹을수 있다
                if distance[cx][cy]+1>option[0]: # 최단거리가 아니면 탐색종료
                    option[1].sort()
                    return option[1][0][0],option[1][0][1],option[0]
                option[0] = distance[cx][cy]+1
                option[1].append((nx,ny))
            else:
                q.append((nx,ny))
                distance[nx][ny] = distance[cx][cy] + 1
    
    if len(option[1]):  # 먹을 고기가 있다
        option[1].sort()
        return option[1][0][0],option[1][0][1],option[0]
    return -1,-1,0      # 없다

dx = [-1,0,1,0]
dy = [0,-1,0,1]
N = int(input())
table = []
for i in range(N):
    table.append(list(map(int,input().split())))
    for j in range(N):
        if table[i][j] == 9:    
            x,y = i,j   # 상어 위치

size = 2    # 처음 크기
count = 0   # 먹은 고기수
answer = 0  # 총 시간
while True:
    table[x][y] = 0
    x,y,t = find_fish(x,y)
    if x==-1:   # 먹을 고기가 없다
        break
    if count+1==size:   # 크기 증가
        size += 1
        count = 0
    else:
        count += 1      # 크기 그대로
    answer += t
print(answer)