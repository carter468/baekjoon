# 개미
# Platinum 5, DFS, binary search

import sys,bisect
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def solve(x,px):
    idx = bisect.bisect_right(dist,dist[-1]-energy[x-1]-1)
    result[x] = path[idx]
    for nx,d in graph[x]:
        if nx != px:
            dist.append(dist[-1]+d)
            path.append(nx)
            solve(nx,x)
            dist.pop()
            path.pop()

N = int(input())
energy = [int(input()) for _ in range(N)]
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

result = [1]*(N+1)
dist = [0]
path = [1]
solve(1,1)
print(*result[1:],sep='\n')