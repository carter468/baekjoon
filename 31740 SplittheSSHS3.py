# Split the SSHS 3
# Gold 4, DFS

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def DFS(x,prev):
    global m
    c = W[x-1]
    for nx in graph[x]:
        if nx != prev:
            c += DFS(nx,x)
    d = abs(c*2-p)
    if d < m[0]: m = [d,x,prev]
    return c

N = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
W = [int(input()) for _ in range(N)]

p = sum(W)
m = [10**10,0,0]
for x in graph[1]:
    DFS(x,1)
print(m[0])
print(m[1],m[2])