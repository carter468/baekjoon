# 그래프 매칭
# Gold 3, DP

def DP(M):
    # dp[i][j][k] : i번째 정점, 첫번째 정점 간선 여부, 현재 정점 간선 여부
    dp = [[[0]*2 for _ in range(2)] for _ in range(M)]
    dp[0][0][0] = 1
    dp[0][1][1] = 1

    for i in range(1,M-1):
        for j in range(2):
            dp[i][j][0] += sum(dp[i-1][j])
            dp[i][j][1] += dp[i-1][j][0]
    dp[-1][0][0] += sum(dp[-2][0])
    dp[-1][0][1] += dp[-2][0][0]
    dp[-1][1][0] += sum(dp[-2][1])

    return sum(dp[-1][0])+sum(dp[-1][1])

while True:
    try:
        print(DP(int(input())))
    except:
        break