# 게임
# Gold 2, DP, DFS

import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

n,m = map(int,input().split())
arr = [input() for _ in range(n)]

def dfs(x,y,cnt):
    global result
    result = max(result,cnt)
    k = int(arr[x][y])
    for nx,ny in (x+k,y),(x-k,y),(x,y+k),(x,y-k):
        if (nx,ny) in visited:
            print(-1)
            exit()
        if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] != 'H' and cnt+1 > dp[nx][ny]:
            dp[nx][ny] = cnt+1
            visited.add((nx,ny))
            dfs(nx,ny,cnt+1)
            visited.remove((nx,ny))
    
dp = [[0]*m for _ in range(n)]
result = 0
visited = {(0,0)}
dfs(0,0,0)
print(result+1)