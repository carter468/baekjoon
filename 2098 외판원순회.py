# 외판원 순회

import sys
input = sys.stdin.readline

def dfs(x,visited):
    if dp[x][visited] != 0:
        return dp[x][visited]
    if visited == (1<<N) - 1:
        if cost[x][0]:
            return cost[x][0]
        else:
            return INF

    temp = INF
    for i in range(1,N):
        if not visited&(1<<i) and cost[x][i] != 0:
            dist = dfs(i,visited|(1<<i)) + cost[x][i]
            if temp > dist:
                temp = dist
    dp[x][visited] = temp
    return dp[x][visited]

N = int(input())
cost = []
for _ in range(N):
    cost.append(list(map(int,input().split())))

INF = int(10**9)
dp = [[0]*(1<<N) for _ in range(N)]

print(dfs(0,1))