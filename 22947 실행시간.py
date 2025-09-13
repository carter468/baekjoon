# 실행 시간
# Gold 2, topological sorting, bruteforcing

from collections import deque
import itertools

def run_task(indegree,c):
    dist = [0]*(N+1)
    dist[1] = T[1]
    q = deque([1])
    while q:
        x = q.popleft()
        for nx in graph[x]:
            if nx in c:
                t = 0
            else:
                t = T[nx]
            dist[nx] = max(dist[nx],dist[x]+t)
            indegree[nx] -= 1
            if indegree[nx] == 0:
                q.append(nx)
    return dist,x

N,M,K = map(int,input().split())
T = [0]+list(map(int,input().split()))

graph = [[] for _ in range(N+1)]
indegree = [0]*(N+1)
for _ in range(M):
    s,e = map(int,input().split())
    graph[s].append(e)
    indegree[e] += 1

E = run_task(indegree[:],[])[1]
min_t = 10**9
for c in itertools.combinations(range(2,N+1),K):
    if E in c: continue
    dist = run_task(indegree[:],c)[0]
    min_t = min(min_t,dist[E])
print(min_t)