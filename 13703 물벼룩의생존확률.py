# 물벼룩의 생존확률
# Gold 5, 다이나믹 프로그래밍

k,n = map(int,input().split())

dp = [[0]*(n+1) for _ in range(65)] 
dp[k][0] = 1
for j in range(n): 
    for i in range(1,n-j+1):   
        dp[i+1][j+1] += dp[i][j]
        dp[i-1][j+1] += dp[i][j]

answer = 2**n
for i in range(n+1):
    answer -= 2**(n-i)*dp[0][i]
print(answer)