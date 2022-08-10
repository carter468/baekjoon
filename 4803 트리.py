# 트리

import sys
input = sys.stdin.readline

def bfs(x):
    result = True
    q = [x]
    while q:
        k = q.pop(0)
        if visited[k] == 1:
            result = False
        visited[k] = 1
        for j in graph[k]:
            if visited[j] == 0:
                q.append(j)
    return result

case = 0
while True:
    case += 1
    n,m = map(int,input().split())
    if n==0 and m==0:
        break
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a,b = map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)
    cnt = 0
    visited = [0]*(n+1)
    for i in range(1,n+1):
        if visited[i] == 1:
            continue
        if bfs(i) == True:
            cnt += 1
    if cnt == 0:
        print('Case {}: No Trees.'.format(case))
    elif cnt == 1:
        print('Case {}: There is one tree.'.format(case))
    else:
        print('Case {}: A forest of {} trees.'.format(case,cnt))