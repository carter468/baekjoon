# 내리막길

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

m,n = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(m)]

dp = [[-1]*n for _ in range(m)]
dx,dy = [-1,1,0,0],[0,0,-1,1] #상, 하, 좌, 우

def dfs(x,y):
    if x==m-1 and y==n-1:   #출발점
        return 1
    if dp[x][y] != -1:      #이미 탐색한 지점
        return dp[x][y]
    dp[x][y] = 0
    for i in range(4):      #4방향 탐색
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<=nx<m and 0<=ny<n:
            if arr[nx][ny] < arr[x][y]: 
                dp[x][y] += dfs(nx,ny)
    return dp[x][y]

print(dfs(0,0))