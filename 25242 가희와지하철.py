# 가희와 지하철
# Platinum 5, BFS

from collections import deque
import sys
input = sys.stdin.readline
INF = sys.maxsize

N,Q = map(int,input().split())

idx = 0
st_num = dict()
pos = dict()
transfer = set()
graph = [[] for _ in range(200000)]
for l in range(N):
    n,*arr = input().split()
    x = arr[0]
    if x in pos:
        transfer.add(x)
    else:
        st_num[x] = idx
        idx += 1
        pos[x] = l,0
    
    for i in range(1,int(n)):
        x = arr[i]
        if x in pos:
            transfer.add(x)
        else:
            st_num[x] = idx
            idx += 1
        a = st_num[arr[i-1]]
        b = st_num[x]
        graph[a].append(b)
        graph[b].append(a)
        pos[x] = l,i

dist = dict()
for t in transfer:
    s = st_num[t]
    q = deque([s])
    visited = [INF]*idx
    visited[s] = 0
    while q:
        x = q.popleft()
        for nx in graph[x]:
            if visited[nx] == INF:
                visited[nx] = visited[x]+2
                q.append(nx)
    dist[t] = visited

for _ in range(Q):
    s,e = input().split()
    min_val = INF
    if pos[s][0] == pos[e][0]:
        min_val = abs(pos[s][1]-pos[e][1])*2
    for t in transfer:
        min_val = min(min_val,dist[t][st_num[s]]+dist[t][st_num[e]])

    print(min_val if min_val < INF else -1)