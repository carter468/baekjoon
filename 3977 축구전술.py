# 축구 전술

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(x):
    visited[x] = 1
    for i in graph[x]:
        if visited[i] == 0:
            dfs(i)
    stack.append(x)

def dfs_r(x):
    global idid
    visited[x] = 1
    ids[x] = idid
    scc.append(x)
    for i in graph_r[x]:
        if visited[i] == 0:
            dfs_r(i)

t = int(input())
while t:
    inp = input()
    if inp == '\n':
        continue
    n,m = map(int,inp.split())
    graph = [[] for _ in range(n)]
    graph_r = [[] for _ in range(n)]
    for _ in range(m):
        a,b = map(int,input().split())
        graph[a].append(b)
        graph_r[b].append(a)
    stack = []
    visited = [0]*n
    for i in range(n):
        if visited[i] == 0:
            dfs(i)
    idid = -1
    ids = [-1]*n
    visited = [0]*n
    result = [[] for _ in range(n)]
    while stack:
        scc = []
        x = stack.pop()
        if visited[x] == 0:
            idid += 1
            dfs_r(x)
            result[idid] = scc
    indegree = [0]*(idid+1)
    for i in range(n):
        for x in graph[i]:
            if ids[i] != ids[x]:
                indegree[ids[x]] += 1
    tmp = []
    cnt = 0
    for i in range(len(indegree)):
        if indegree[i] == 0:
            for j in result[i]:
                tmp.append(j)
            cnt += 1
    if cnt == 1:
        for i in sorted(tmp):
            print(i)
    else:
        print('Confused')
    print()
    t -= 1