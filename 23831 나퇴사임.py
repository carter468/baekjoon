# 나 퇴사임?
# Gold 3, DP

N = int(input())
A,B = map(int,input().split())
arr = [tuple(map(int,input().split())) for _ in range(N)]

# i번째 날 자습 j번했고 요양원은 k번 갔고 마지막은 휴게실인지 아닌지 
dp = [[[[0]*2 for _ in range(A+1)] for _ in range(N+1)] for _ in range(N+1)]

for i in range(N):
    c = max(arr[i][0],arr[i][1])
    d = arr[i][2]
    e = arr[i][3]
    for j in range(i+1):
        for k in range(A+1):
            dp[i+1][j+1][k][0] = max(dp[i+1][j+1][k][0],max(dp[i][j][k])+c) # 자습
            dp[i+1][j][k][1] = max(dp[i+1][j][k][1],dp[i][j][k][0]+d) # 휴게실
            if k != A:
                dp[i+1][j][k+1][0] = max(dp[i+1][j][k+1][0],max(dp[i][j][k])+e) # 요양

result = 0
for i in range(B,N+1):
    for j in range(A+1):
        result = max(result,max(dp[N][i][j]))
print(result)