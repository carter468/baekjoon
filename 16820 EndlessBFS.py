# Endless BFS
# Platinum 5, BFS

from collections import deque
import sys
input = sys.stdin.readline

def solve():
    N,M = map(int,input().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        u,v = map(int,input().split())
        graph[u].append(v)
        graph[v].append(u)

    visited = [[False,False] for _ in range(N+1)]
    visited[1][0] = True
    count = [1,0]
    q = deque([(1,0)])
    while q:
        x,d = q.popleft()
        nd = d+1
        for nx in graph[x]:
            if visited[nx][nd%2] == False:
                visited[nx][nd%2] = True
                q.append((nx,nd))
                count[nd%2] += 1
                if count[nd%2] == N: return nd
    return -1

print(solve())