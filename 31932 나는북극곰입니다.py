# 나는 북극곰입니다
# Gold 2, dijkstra, binary search

import sys,heapq
input = sys.stdin.readline

def check(k):
    dist = [sys.maxsize]*(N+1)
    dist[1] = 0
    q = [(0,1)]
    while q:
        d,x = heapq.heappop(q)
        if x == N: return True
        if d > dist[x]: continue
        for nx,dd,t in graph[x]:
            nd = d+dd
            if nd < dist[nx] and nd+k <= t:
                dist[nx] = nd
                heapq.heappush(q,(nd,nx))
    return False

N,M = map(int,input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    u,v,d,t = map(int,input().split())
    graph[u].append((v,d,t))
    graph[v].append((u,d,t))

if not check(0): exit(print(-1))
lo,hi = 0,10**9
while lo+1 < hi:
    mid = (lo+hi)//2
    if check(mid): lo = mid
    else: hi = mid
print(lo)