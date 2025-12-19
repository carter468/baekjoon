# 행렬 곱셈
# Platinum 5, eulerian path, DFS

import sys
input = sys.stdin.readline

graph = [set() for _ in range(1001)]
indegree = [0]*1001
outdegree = [0]*1001
s1,s2,s3,s4 = set(),set(),set(),set()
for _ in range(int(input())):
    r,c = map(int,input().split())
    graph[r].add(c)
    graph[c].add(r)
    outdegree[r] += 1
    indegree[c] += 1
    for x in (r,c):
        s1.discard(x)
        s2.discard(x)
        s3.discard(x)
        s4.discard(x)
        if indegree[x]+1 == outdegree[x]:
            s1.add(x)
        elif indegree[x] == outdegree[x]+1:
            s2.add(x)
        elif indegree[x] == outdegree[x]:
            s3.add(x)
        else:
            s4.add(x)
    
    q = [r]
    v = {r}
    while q:
        x = q.pop()
        for nx in graph[x]:
            if nx not in v:
                v.add(nx)
                q.append(nx)
    
    if len(v) != len(s1)+len(s2)+len(s3)+len(s4):
        print(0)
        continue

    if s4:
        print(0)
    elif not s1 and not s2:
        print(max(s3)**2)
    elif len(s1) == 1 and len(s2) == 1:
        print(max(s1)*max(s2))
    else:
        print(0)