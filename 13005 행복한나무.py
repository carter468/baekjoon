# 행복한 나무
# Platinum 5, DFS

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def solve(x,a,b):
    global count

    if a-b > A[x-1]:
        q = [x]
        while q:
            x = q.pop()
            count += 1
            for nx,_ in graph[x]:
                q.append(nx)
        return
    
    for nx,c in graph[x]:
        solve(nx,a+c,min(a,b))

N = int(input())
A = tuple(map(int,input().split()))
graph = [[] for _ in range(N+1)]
for i in range(2,N+1):
    p,c = map(int,input().split())
    graph[p].append((i,c))

count = 0
solve(1,0,0)
print(count)