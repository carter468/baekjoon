# 나이트가 체스판을 벗어나지 않을 확률
# Gold 4, DP

N,x,y,K = map(int,input().split())

dp = [[[0]*N for _ in range(N)] for _ in range(K+1)]
dp[0][x-1][y-1] = 1

for i in range(K):
    for j in range(N):
        for k in range(N):
            for dx,dy in (1,2),(2,1),(2,-1),(1,-2),(-1,-2),(-2,-1),(-2,1),(-1,2):
                nx,ny = j+dx,k+dy
                if 0 <= nx < N and 0 <= ny < N:
                    dp[i+1][nx][ny] += dp[i][j][k]/8

result = 0
for i in range(N):
    for j in range(N):
        result += dp[K][i][j]
print(result)