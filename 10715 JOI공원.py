# JOI 공원
# Gold 1, dijkstra, prefix sum

from collections import defaultdict
import sys,heapq
input = sys.stdin.readline

N,M,C = map(int,input().split())
road = [tuple(map(int,input().split())) for _ in range(M)]
graph = [[] for _ in range(N+1)]
total_len = 0
for a,b,d in road:
    graph[a].append((b,d))
    graph[b].append((a,d))
    total_len += d

dist = [10**10]*(N+1)
dist[1] = 0
q = [(0,1)]
while q:
    d,x = heapq.heappop(q)
    if d > dist[x]: continue
    for nx,dd in graph[x]:
        nd = d+dd
        if nd < dist[nx]:
            dist[nx] = nd
            heapq.heappush(q,(nd,nx))

arr = set()
length = defaultdict(int)
length[0] = 0
for a,b,d in road:
    k = max(dist[a],dist[b])
    length[k] += d
    arr.add(k)
arr = sorted(arr)
for i in range(len(arr)-1):
    length[arr[i+1]] += length[arr[i]]

minval = 1<<70
for c in length:
    minval = min(minval,C*c+total_len-length[c])
print(minval)