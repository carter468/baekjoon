# 문자열 지옥에 빠진 호석
# Gold 4, DFS, hash set

from collections import defaultdict
import sys
input = sys.stdin.readline

def dfs(x,y,s):
    count[s] += 1
    if len(s) == 5: return

    for nx,ny in (x+1,y),(x+1,y+1),(x+1,y-1),(x,y+1),(x,y-1),(x-1,y+1),(x-1,y),(x-1,y-1):
        nx %= n
        ny %= m
        dfs(nx,ny,s+arr[nx][ny])

n,m,k = map(int,input().split())
arr = [input().strip() for _ in range(n)]
count = defaultdict(int)

for i in range(n):
    for j in range(m):
        dfs(i,j,arr[i][j])

for _ in range(k):
    print(count[input().strip()])