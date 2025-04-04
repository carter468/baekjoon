# 택배 상하차는 힘들어
# Gold 2, DFS, tree DP

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def solve(x):
    global result
    count = []
    for nx in graph[x]:
        if not visited[nx]:
            visited[nx] = True
            count.append(solve(nx))
    result += sum(sorted(count)[:-1])
    return arr[x-1]+sum(count)

N = int(input())
arr = tuple(map(int,input().split()))
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    i,j = map(int,input().split())
    graph[i].append(j)
    graph[j].append(i)

visited = [False]*(N+1)
visited[1] = True
result = sum(arr[1:])
for x in graph[1]:
    visited[x] = True
    solve(x)
print(result*2)