# 단지번호붙이기

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n = int(input())
arr = []
for _ in range(n):
    arr.append(str(input().strip()))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

visited = [[0] * n for _ in range(n)]

cmplx = []

def dfs(x,y):
    global cnt
    cnt += 1

    visited[x][y] = 1

    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
            # 좌표가 지도 안에 있고     집이 있고           방문기록이 없다면
        if 0<=nx<n and 0<=ny<n and arr[nx][ny]=='1' and visited[nx][ny]==0:
            dfs(nx,ny)      # 방문

for i in range(n):
    for j in range(n):
        if arr[i][j]=='1' and visited[i][j]==0: #집이 있고 방문기록이 없다면 방문
            cnt = 0             # 집의 수 초기화
            dfs(i,j)
            cmplx.append(cnt)   # 단지 내 집의 수   

print(len(cmplx))
cmplx.sort()
for x in cmplx:
    print(x)