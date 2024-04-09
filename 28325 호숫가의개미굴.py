# 호숫가의 개미굴
# Gold 5, DP

n = int(input())
arr = tuple(map(int,input().split()))

dp = [[[0]*2 for _ in range(2)] for _ in range(n-1)]
dp[0][0][0] = arr[0] 
dp[0][1][1] = 1     
for i in range(1,n-1):
    dp[i][0][0] = max(dp[i-1][0])+arr[i]
    dp[i][1][0] = max(dp[i-1][1])+arr[i]
    dp[i][0][1] = dp[i-1][0][0]+1
    dp[i][1][1] = dp[i-1][1][0]+1
print(max(dp[-1][0][0]+max(1,arr[-1]),dp[-1][0][1]+arr[-1],max(dp[-1][1])+arr[-1]))