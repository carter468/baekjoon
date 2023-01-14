# 동전 문제
# Gold 2, 다이나믹 프로그래밍, 그리디 알고리즘

import sys
input = sys.stdin.readline

dp = [0]*100
dp[1] = 1
for i in range(2,100):
    dp[i] = dp[i-1]+1
    if i>=10:
        dp[i] = min(dp[i],dp[i-10]+1)
    if i>=25:
        dp[i] = min(dp[i],dp[i-25]+1)
print(dp)

for _ in range(int(input())):
    n = input().strip().zfill(16)
    answer = 0
    for i in range(8):
        answer += dp[int(n[i*2:i*2+2])]
    print(answer)