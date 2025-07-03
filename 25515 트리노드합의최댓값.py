# 트리 노드 합의 최댓값
# Gold 4, DFS

import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

def dfs(x):
    t = s[x]
    for nx in graph[x]:
        t += dfs(nx)
    return t if x == 0 else max(0,t)

N = int(input())
graph = [[] for _ in range(N)]
for _ in range(N-1):
    p,c = map(int,input().split())
    graph[p].append(c)
s = tuple(map(int,input().split()))

print(dfs(0))