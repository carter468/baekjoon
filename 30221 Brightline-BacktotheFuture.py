# Brightline - Back to the Future
# Gold 4, bellman-ford

import sys
input = sys.stdin.readline
INF = 10**9

N,M = map(int,input().split())
edge = []
for _ in range(M):
    a,b,c,d = input().split()
    d = int(d)
    if c == 'r': d = -d
    edge.append((int(a),int(b),d))

dist = [INF]*(N+1)
dist[1] = 0
for _ in range(N-1):
    for s,e,d in edge:
        if dist[s] != INF and dist[e] > dist[s]+d:
            dist[e] = dist[s]+d

print(*[i for i in range(N+1) if dist[i] < 0],sep='\n')