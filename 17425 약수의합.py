# 약수의 합
# Gold 4, 수학

import sys
input = sys.stdin.readline
MAX = 10**6

dp = [0]+[1]*MAX
for i in range(2, MAX+1):
    j = 1
    while i*j <= MAX:
        dp[i*j] += i
        j += 1
for i in range(1, MAX+1):
    dp[i] += dp[i-1]

for _ in range(int(input())):
    print(dp[int(input())])