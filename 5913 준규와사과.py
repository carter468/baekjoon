# 준규와 사과
# Gold 4, 백트래킹

import sys
input = sys.stdin.readline

def dfs(x,y,count):
    global result
    if (x,y) == (4,4):
        if count == 25-k: result += 1
        return
    for nx,ny in ((x+1,y),(x-1,y),(x,y+1),(x,y-1)):
        if 0<=nx<5 and 0<=ny<5 and visit[nx][ny] == False and grid[nx][ny] == 1:
            visit[nx][ny] = True
            dfs(nx,ny,count+1)
            visit[nx][ny] = False

grid = [[1]*5 for _ in range(5)]
visit = [[False]*5 for _ in range(5)]
visit[0][0] = True
k = int(input())
for _ in range(k):
    a,b = map(int,input().split())
    grid[a-1][b-1] = 0

result = 0
dfs(0,0,1)
print(result)

# import sys
# input = sys.stdin.readline

# def check():
#     for i in range(5):
#         for j in range(5):
#             if visit[i][j] == False:
#                 return False
#     return True

# def dfs(x,y,count):
#     global result
#     if (x,y) == (4,4):
#         if check(): result += count%2
#         return
#     for nx,ny in ((x+1,y),(x-1,y),(x,y+1),(x,y-1)):
#         if 0<=nx<5 and 0<=ny<5 and visit[nx][ny] == False and grid[nx][ny] == 1:
#             visit[nx][ny] = True
#             dfs(nx,ny,count+1)
#             visit[nx][ny] = False

# grid = [[1]*5 for _ in range(5)]
# visit = [[False]*5 for _ in range(5)]
# visit[0][0] = True
# for _ in range(int(input())):
#     a,b = map(int,input().split())
#     grid[a-1][b-1] = 0
#     visit[a-1][b-1] = True

# result = 0
# dfs(0,0,1)
# print(result)