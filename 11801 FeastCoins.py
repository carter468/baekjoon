# Feast Coins
# Gold 1, DP, knapsack

import sys
input = sys.stdin.readline

def solve(M,C):
    dp = [1]+[0]*M

    for i in range(N):
        v,c = coin[i]
        if c < C: continue
        for j in range(M,v-1,-1):
            dp[j] += dp[j-v]
            
    return dp[M]

for t in range(int(input())):
    S,N = map(int,input().split())
    coin = [tuple(map(int,input().split())) for _ in range(N)]

    result = 0
    for i in range(1,int(S**0.5)+1):
        if S%i == 0:
            result += solve(S//i,i)
            if i*i != S:
                result += solve(i,S//i)
    print(f'Case {t+1}: {result}')