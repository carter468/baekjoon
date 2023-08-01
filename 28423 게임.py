# 게임
# Gold 4, DFS

import sys
sys.setrecursionlimit(10**6)

def dfs(x):
    nx = fx(x)
    if nx > 100000: return -1
    elif nx == x: return 1
    elif nx in visit: return 0
    elif g[nx] != 2: return g[nx]
    else:
        visit.add(nx) 
        g[nx] = dfs(nx)
        return g[nx]

def fx(n):
    a,b = 0,1
    for i in str(n):
        a += int(i)
        b *= int(i)
    return int(str(a)+str(b))

g = [2]*100001
for i in range(1,100001):
    if g[i] == 2:
        visit = set([i])
        g[i] = dfs(i)

l,r = map(int,input().split())
print(sum(g[l:r+1]))