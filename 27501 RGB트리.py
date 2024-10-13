# RGB트리
# Gold 1, DP

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def solve(x,prev,c):
    if dp[x][c]: return dp[x][c]
    dp[x][c] = arr[x][c]
    for nx in graph[x]:
        if nx != prev:
            dp[x][c] += max(solve(nx,x,(c+1)%3),solve(nx,x,(c+2)%3))
    return dp[x][c]

def color(x,c):
    c1,c2 = (c+1)%3,(c+2)%3
    for nx in graph[x]:
        if result[nx] == 0:
            if dp[nx][c1] >= dp[nx][c2]:
                result[nx] = 'RGB'[c1]
                color(nx,c1)
            else:
                result[nx] = 'RGB'[c2]
                color(nx,c2)

n = int(input())
graph = [[] for _ in range(n)]
for _ in range(n-1):
    a,b = map(int,input().split())
    a,b = a-1,b-1
    graph[a].append(b)
    graph[b].append(a)
arr = [tuple(map(int,input().split())) for _ in range(n)]

dp = [[0]*3 for _ in range(n)]
for i in range(3):
    solve(0,-1,i)
result = [0]*n
for i in range(3):
    if dp[0][i] == max(dp[0]):
        result[0] = 'RGB'[i]
        color(0,i)
        break
print(max(dp[0]))
print(''.join(result))