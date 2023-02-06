# 퍼레이드
# Gold 4, 한붓그리기, 분리집합

import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

def dfs(node):
    visit[node] = 1
    for nn in graph[node]:
        if not visit[nn]:
            dfs(nn)

V,E = map(int,input().split())
point = [1]*(V+1)
graph = [[] for _ in range(V+1)]
for _ in range(E):
    a,b = map(int,input().split())
    point[a]*=-1
    point[b]*=-1
    graph[a].append(b)
    graph[b].append(a)

visit = [1]+[0]*V
dfs(1)
print('NO' if point.count(-1)>2 or 0 in visit else 'YES')