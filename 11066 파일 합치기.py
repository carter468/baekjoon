# 파일 합치기
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t): 
    n = int(input())
    sizes = [0] + list(map(int,input().split()))
    s = [0 for _ in range(n+1)]
    for i in range(1,n+1):
        s[i] = s[i-1] + sizes[i]

    dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
    for i in range(2,n+1):
        for j in range(1,n+2-i):
            dp[j][j+i-1] = min([dp[j][j+k] + dp[j+k+1][j+i-1] for k in range(i-1)]) + (s[j+i-1]-s[j-1])

    print(dp[1][n])