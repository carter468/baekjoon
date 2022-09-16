# 합성함수와 쿼리

import sys
import math
input = sys.stdin.readline

m = int(input())
l = int(math.log2(500000))+1      # 최대 n : 500000

dp = [[0 for _ in range(m+1)] for _ in range(l)]  # 희소배열
dp[0] = [0]+list(map(int,input().split()))
for i in range(1,l):
    for j in range(m+1):
        dp[i][j] = dp[i-1][dp[i-1][j]]

q = int(input())
for _ in range(q):
    n,x = map(int,input().split())
    i = 0
    while n != 0:
        if n % 2 == 1:
            x = dp[i][x]
        n //= 2
        i += 1
    print(x)