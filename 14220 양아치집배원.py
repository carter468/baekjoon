# 양아치 집배원
# Gold 3, DP

INF = 10**9

N = int(input())
arr = [tuple(map(int,input().split())) for _ in range(N)]

dp = [0]*N
for _ in range(N-1):
    ndp = [INF]*N
    for i in range(N):
        for j in range(N):
            if arr[i][j] > 0:
                ndp[j] = min(ndp[j],dp[i]+arr[i][j])
    dp = ndp

m = min(dp)
print(m if m < INF else -1)