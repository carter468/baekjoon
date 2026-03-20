# 군사 이동
# Gold 3, binary search, DFS

import sys
input = sys.stdin.readline

def check(x):
    visited = {S}
    q = [S]
    while q:
        u = q.pop()
        if u == E: return True
        for v,w in graph[u]:
            if w >= x and v not in visited:
                visited.add(v)
                q.append(v)
    return False

P,W = map(int,input().split())
S,E = map(int,input().split())
graph = [[] for _ in range(P)]
for _ in range(W):
    u,v,w = map(int,input().split())
    graph[u].append((v,w))
    graph[v].append((u,w))

yes,no = 1,1111
while yes+1 < no:
    mid = (yes+no)//2
    if check(mid): yes = mid
    else: no = mid
print(yes)