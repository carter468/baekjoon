# 맥주 마시면서 걸어가기
# Gold 5, DFS

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    arr = [tuple(map(int,input().split())) for _ in range(n+2)]

    graph = [[] for _ in range(n+2)]
    for i in range(n+2):
        for j in range(n+2):
            if i == j: continue
            a,b = arr[i]
            c,d = arr[j]
            if abs(a-c)+abs(b-d) <= 1000:
                graph[i].append(j)
                graph[j].append(i)
    
    visited = [False]*(n+2)
    visited[0] = True
    q = [0]
    while q:
        x = q.pop()
        if x == n+1:
            print('happy')
            break
        for nx in graph[x]:
            if not visited[nx]:
                visited[nx] = True
                q.append(nx)
    else: print('sad')