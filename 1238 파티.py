# 파티
# Gold 3, dijkstra

# 908ms n번의 dijkstra
# import sys,heapq
# input = sys.stdin.readline

# def dijkstra(start):
#     q = [(0,start)]
#     dist = [10**9]*(n+1)
#     dist[start] = 0
#     while q:
#         d,l = heapq.heappop(q)
#         if dist[l] < d: continue
#         for dd,nl in graph[l]:
#             nd = d+dd
#             if nd < dist[nl]:
#                 dist[nl] = nd
#                 heapq.heappush(q,(nd,nl))
#     return dist

# n,m,x = map(int,input().split())
# graph = [[] for _ in range(n+1)]
# for _ in range(m):
#     s,e,t = map(int,input().split())
#     graph[s].append((t,e))

# dist = dijkstra(x)
# result = 0
# for i in range(1,n+1):
#     result = max(result,dijkstra(i)[x]+dist[i])
# print(result)

# 68ms 2번의 dijkstra
import sys,heapq
input = sys.stdin.readline

def dijkstra(graph):
    q = [(0,x)]
    dist = [10**9]*(n+1)
    dist[x] = 0
    while q:
        d,l = heapq.heappop(q)
        if dist[l] < d: continue
        for dd,nl in graph[l]:
            nd = d+dd
            if nd < dist[nl]:
                dist[nl] = nd
                heapq.heappush(q,(nd,nl))
    return dist

n,m,x = map(int,input().split())
graph = [[] for _ in range(n+1)]
graph_rev = [[] for _ in range(n+1)]
for _ in range(m):
    s,e,t = map(int,input().split())
    graph[s].append((t,e))
    graph_rev[e].append((t,s))

dist = dijkstra(graph)
dist_rev = dijkstra(graph_rev)
result = 0
for i in range(1,n+1):
    result = max(result,dist[i]+dist_rev[i])
print(result)