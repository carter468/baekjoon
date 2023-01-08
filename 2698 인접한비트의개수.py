# 인접한 비트의 개수
# Gold 4, 다이나믹 프로그래밍

import sys
input = sys.stdin.readline

dp = [[[0,0] for _ in range(101)] for _ in range(101)]  # 길이, 1의 개수, 마지막원소
dp[1][0][0] = 1
dp[1][0][1] = 1
for i in range(2,101):  
    for j in range(i):  
        dp[i][j][0] = dp[i-1][j][0]+dp[i-1][j][1]
        dp[i][j][1] = dp[i-1][j][0]+dp[i-1][j-1][1]

for _ in range(int(input())):
    n,k = map(int,input().split())
    print(sum(dp[n][k]))