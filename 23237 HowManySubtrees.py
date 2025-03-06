# How Many Subtrees?
# Gold 4, DFS

import sys
input = sys.stdin.readline

def solve(x):
    for nx in graph[x]:
        if not visited[nx]:
            visited[nx] = True
            result[x] *= solve(nx)+1
    return result[x]

t = 1
while True:
    if (V:=int(input())) == 0: break
    graph = [[] for _ in range(V)]
    for _ in range(V-1):
        a,b = map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)
    
    result = [1]*V
    visited = [False]*V
    visited[0] = True
    solve(0)

    print(f'Case {t}: {sum(result)}')
    t += 1