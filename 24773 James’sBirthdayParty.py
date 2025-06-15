# James’s Birthday Party 
# Gold 5, bruteforcing, DFS

import sys
input = sys.stdin.readline

while True:
    p,c = map(int,input().split())
    if p == 0: break
    
    edge = [tuple(map(int,input().split())) for _ in range(c)]

    for i in range(c):
        graph = [[] for _ in range(p)]
        for j in range(c):
            if i != j:
                a,b = edge[j]
                graph[a].append(b)
                graph[b].append(a)
        
        q = [0]
        visited = [False]*p
        visited[0] = True
        while q:
            x = q.pop()
            for nx in graph[x]:
                if not visited[nx]:
                    visited[nx] = True
                    q.append(nx)
        
        if any(x == False for x in visited):
            print('Yes')
            break
    else: print('No')