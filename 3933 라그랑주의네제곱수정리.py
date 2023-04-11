# 라그랑주의 네 제곱수 정리
# Gold 5, DP

import sys
input = sys.stdin.readline
MAX = 2**15

dp = [[0]*4 for _ in range(MAX+1)]
for i in range(1,int(MAX**0.5)+1):
    dp[i*i][0] = 1
    for j in range(i*i+1,MAX+1):
        for k in range(3):
            dp[j][k+1] += dp[j-i*i][k]

while n:=int(input()):
    print(sum(dp[n]))