# 기숙사 재배정
# Gold 2, DP

import sys
input = sys.stdin.readline

dp = [0]*21
dp[2] = 1
for i in range(3,21):
    dp[i] = (dp[i-1]+dp[i-2])*(i-1)

for _ in range(int(input())):
    print(dp[int(input())])