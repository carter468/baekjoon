# 중량제한
# Gold 3, binary search, DFS

import sys
input = sys.stdin.readline

def check(k):
    visited = [False]*(n+1)
    visited[s] = True
    q = [s]
    while q:
        x = q.pop()
        if x == e: return True
        for nx,c in graph[x]:
            if not visited[nx] and c >= k:
                visited[nx] = True
                q.append(nx)
    return False

n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))
s,e = map(int,input().split())

lo,hi = 0,10**9+1
while lo+1 < hi:
    mid = (lo+hi)//2
    if check(mid): lo = mid
    else: hi = mid
print(lo)
