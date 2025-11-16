# 이번 시험 다들 다양한 방식으로 망쳤나 봐
# Platinum 3, DFS, SCC

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def tarjan_scc(N):
    index = 0
    stack = []
    indices = [-1]*N
    lowlink = [0]*N
    on_stack = [False]*N
    sccs = []

    def strongconnect(v):
        nonlocal index
        indices[v] = lowlink[v] = index
        index += 1
        stack.append(v)
        on_stack[v] = True

        for w in graph[v]:
            if indices[w] == -1:
                strongconnect(w)
                lowlink[v] = min(lowlink[v],lowlink[w])
            elif on_stack[w]:
                lowlink[v] = min(lowlink[v],indices[w])

        if lowlink[v] == indices[v]:
            scc = []
            while True:
                w = stack.pop()
                on_stack[w] = False
                scc.append(w)
                if w == v:
                    break
            sccs.append(scc)

    for v in range(N):
        if indices[v] == -1:
            strongconnect(v)

    return sccs

N,M,X = map(int,input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    x,y = map(int,input().split())
    graph[x].append(y)

result = N
visited = [False]*(N+1)
visited[X] = True
q = [X]
while q:
    x = q.pop()
    result -= 1
    for nx in graph[x]:
        if not visited[nx]:
            visited[nx] = True
            q.append(nx)

sccs = tarjan_scc(N+1)
for scc in sccs:
    if not visited[scc[0]]:
        result -= len(scc)-1
print(result)