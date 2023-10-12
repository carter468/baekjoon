# 색칠하기
# Gold 5, DFS

import sys
input = sys.stdin.readline

def dfs(i):
    visit[i] = 1
    q = [i]
    while q:
        x = q.pop()
        for nx in graph[x]:
            if visit[nx] == 0:
                visit[nx] = -visit[x]
                q.append(nx)
            elif visit[nx] == visit[x]:
                return False
    return True

for _ in range(int(input())):
    n,m = map(int,input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a,b = map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)

    visit = [0]*(n+1)
    for i in range(1,n+1):
        if visit[i] == 0:
            if dfs(i) == False:
                print('impossible')
                break
    else: print('possible')