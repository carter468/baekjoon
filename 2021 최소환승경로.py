# 최소 환승 경로
# Gold 1, bfs

from collections import deque
import sys
input = sys.stdin.readline
L = 10**5

def sol():
    n,l = map(int,input().split())
    graph = [[] for _ in range(n+L+1)]
    for i in range(1,l+1):
        for j in tuple(map(int,input().split()))[:-1]:
            graph[j].append(i+L)
            graph[i+L].append(j)
    s,e = map(int,input().split())
    if s==e: return 0
        
    visit = [-1]*(n+L+1)
    visit[s] = 0
    q = deque([s])
    while q:
        x = q.popleft()
        for nx in graph[x]:
            if visit[nx]!=-1: continue
            if nx>L:
                visit[nx] = visit[x]+1
            else:
                if nx==e: return visit[x]-1
                visit[nx] = visit[x]
            q.append(nx)
    return -1
    
print(sol())