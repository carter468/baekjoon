# 별자리 찾기
# Gold 4, 브루트포스

import sys
input = sys.stdin.readline

def dfs(x,y,count):
    if count == m:
        print(i-a,j-b)
        return
    x,y = i+cst[count][0],j+cst[count][1]
    if (x,y) in star:
        dfs(x,y,count+1)

m = int(input())
cst = [list(map(int,input().split())) for _ in range(m)]
a,b = cst[0]
for i in range(m):
    cst[i][0] -= a
    cst[i][1] -= b

star = set(tuple(map(int,input().split())) for _ in range(int(input())))
for i,j in star:
    dfs(i,j,1)