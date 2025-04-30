# 진우의 달 여행 (Large)
# Gold 5, DP

N,M = map(int,input().split())
arr = [tuple(map(int,input().split())) for _ in range(N)]

dp = [[[10**9]*3 for _ in range(M)] for _ in range(N)]
for j in range(M):
    dp[0][j] = [arr[0][j]]*3
    
for i in range(1,N):
    for j in range(M):
        if j == 0:
            dp[i][j][1] = dp[i-1][j][2]+arr[i][j]
            dp[i][j][2] = min(dp[i-1][j+1][:2])+arr[i][j]
        elif j == M-1:
            dp[i][j][0] = min(dp[i-1][j-1][1:])+arr[i][j]
            dp[i][j][1] = dp[i-1][j][0]+arr[i][j]
        else:
            dp[i][j][0] = min(dp[i-1][j-1][1:])+arr[i][j]
            dp[i][j][1] = min(dp[i-1][j][0],dp[i-1][j][2])+arr[i][j]
            dp[i][j][2] = min(dp[i-1][j+1][:2])+arr[i][j]

result = 10**9
for j in range(M):
    result = min(result,min(dp[-1][j]))
print(result)