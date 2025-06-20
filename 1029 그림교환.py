# 그림 교환
# Gold 1, DP, bitmask

def solve(v,c,p):
    if dp[v][c] != 0: return dp[v][c]

    for i in range(N):
        if (v>>i)&1 == 0 and arr[c][i] >= p:
            dp[v][c] = max(dp[v][c],solve(v|(1<<i),i,arr[c][i])+1)
    return dp[v][c]

N = int(input())
arr = [tuple(map(int,input())) for _ in range(N)]

dp = [[0]*N for _ in range(1<<N)]
print(solve(1,0,0)+1)