# 방법을 출력하지 않는 숫자 맞추기
# Gold 1, DP

import sys
sys.setrecursionlimit(10**6)

def move(idx,left):
    if idx == n:
        return 0
    if dp[idx][left] != 10**9:
        return dp[idx][left]
    
    now = (a[idx]+left)%10
    l = (b[idx]-now)%10
    r = (now-b[idx])%10
    dp[idx][left] = min(dp[idx][left],move(idx+1,(left+l)%10)+l)
    dp[idx][left] = min(dp[idx][left],move(idx+1,left)+r)
    return dp[idx][left]

n = int(input())
a = list(map(int,input()))
b = list(map(int,input()))
dp = [[10**9]*10 for _ in range(n)]

print(move(0,0))