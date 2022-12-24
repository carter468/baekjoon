# 텀 프로젝트
# Gold 3, 깊이 우선 탐색

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(x):
    global group
    visit[x] = True
    cycle.append(x)
    nx = array[x]

    if visit[nx]:
        if nx in cycle:
            group += cycle[cycle.index(nx):]
        return
    else:
        dfs(nx)

for _ in range(int(input())):
    n = int(input())
    array = [0]+list(map(int,input().split()))
    visit = [False]*(n+1)
    group = []
    for i in range(1,n+1):
        if not visit[i]:
            cycle = []
            dfs(i)
    
    print(n-len(group))