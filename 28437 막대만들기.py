# 막대 만들기
# Gold 4, DP

import sys
input = sys.stdin.readline

input()
dp = [0]*100001
for i in map(int,input().split()):
    dp[i] = 1
for i in range(1,100001):
    for j in range(2,100000//i+1):
        dp[i*j] += dp[i]

input()
for x in map(int,input().split()):
    print(dp[x],end=' ')