# Game of Stones
# Platinum 3, sprague-grundy, DFS

import sys
input = sys.stdin.readline

def solve(x):
    if dp[x] != -1: return dp[x]

    s = set()
    for nx in graph[x]:
        s.add(solve(nx))
    
    mex = 0
    while mex in s:
        mex += 1
    
    dp[x] = mex
    return mex

while True:
    N,M = map(int,input().split())
    if N == 0: break
    graph = [[] for _ in range(N)]
    E = tuple(map(int,input().split()))
    for i in range(M):
        graph[E[i*2]].append(E[i*2+1])
    S = tuple(map(int,input().split()))

    dp = [-1]*N
    result = 0
    for i in range(N):
        result ^= solve(i)*(S[i]%2)
    
    print('First' if result else 'Second')