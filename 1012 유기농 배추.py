# 유기농 배추

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def dfs(i,j):
    arr[i][j] = 0
    if i > 0 and arr[i-1][j] == 1:
        dfs(i-1,j)  # 상
    if i < n-1 and arr[i+1][j] == 1:
        dfs(i+1,j)  # 하
    if j > 0 and arr[i][j-1] == 1:
        dfs(i,j-1)  # 좌
    if j < m-1 and arr[i][j+1] == 1:
        dfs(i,j+1)  # 우

t = int(input())
for _ in range(t):
    m,n,k = map(int,input().split())

    arr = [[0]*m for _ in range(n)]
    for _ in range(k):
        a,b = map(int,input().split())
        arr[b][a] = 1

# m,n,k = 10,8,17
# location = [[0,0],[1,0],[1,1],[4,2],[4,3],[4,5],[2,4],[3,4],[7,4],[8,4],[9,4]
# ,[7,5],[8,5],[9,5],[7,6],[8,6],[9,6]]

# arr = [[0]*m for _ in range(n)]
# for x in location:
#     arr[x[1]][x[0]] = 1

    cnt = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1:
                cnt += 1
                dfs(i,j)

    print(cnt)