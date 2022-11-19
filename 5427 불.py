# 불
# Gold 4, 너비 우선 탐색

import sys
input = sys.stdin.readline
from collections import deque

def escape():
    dx = [1,0,0,-1]
    dy = [0,1,-1,0]
    time = 0
    while sang:
        time += 1

        # 불이 번진다
        for _ in range(len(fire)):
            f = fire.popleft()
            for i in range(4):
                nx,ny = f[0]+dx[i],f[1]+dy[i]
                if 0<=nx<h and 0<=ny<w and building_map[nx][ny] == '.':
                    fire.append((nx,ny))
                    building_map[nx][ny] = '*'

        # 안전한곳으로 이동
        for _ in range(len(sang)):
            s = sang.popleft()
            if s[0]==0 or s[0]==h-1 or s[1]==0 or s[1]==w-1: # 탈출구
                return time
            for i in range(4):
                nx,ny = s[0]+dx[i],s[1]+dy[i]
                if 0<=nx<h and 0<=ny<w and building_map[nx][ny] == '.':
                    sang.append((nx,ny))
                    building_map[nx][ny] = '@'
    # 갈 곳이 없다               
    return 'IMPOSSIBLE'

for _ in range(int(input())):
    w,h = map(int,input().split())
    building_map = [list(input()) for _ in range(h)]
    # 불과 상근이 위치 파악
    fire = deque([])
    for i in range(h):
        for j in range(w):
            if building_map[i][j] == '@':
                sang = deque([(i,j)])
            elif building_map[i][j] == '*':
                fire.append((i,j))
    print(escape())