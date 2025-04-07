# 트리의 높이와 너비
# Gold 2, DFS

import sys
input = sys.stdin.readline

def dfs(x,lev):
    global idx
    if x == -1: return
    l,r = arr[x]
    dfs(l,lev+1)
    level[lev].append(idx)
    idx += 1
    dfs(r,lev+1)

N = int(input())
root = set(range(1,N+1))
arr = [None]*(N+1)
for _ in range(N):
    i,l,r = map(int,input().split())
    arr[i] = (l,r)
    if l in root: root.remove(l)
    if r in root: root.remove(r)

level = [[] for _ in range(N+1)]
idx = 0
dfs(root.pop(),1)

result = (0,0)
for i in range(N+1):
    if level[i]:
        x = max(level[i])-min(level[i])+1
        if x > result[1]: result = (i,x)
print(*result)