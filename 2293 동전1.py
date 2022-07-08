# 동전 1

import sys
input = sys.stdin.readline

n,k = map(int,input().split())
value_coin = []
for _ in range(n):
    value_coin.append(int(input()))
dp = [0]*(k+1)      # dp[i] : i 원을 만드는 경우의 수

for x in value_coin:    # 각 동전에 대해서 
    for i in range(1,k+1):  # k 원을 만드는 경우의 수
        if i==x:
            dp[i] += 1
        if i>x:
            dp[i] += dp[i-x]

print(dp[k])
