# 무한 수열 2
# Gold 5, DP

def solve(i):
    if i <= 0: return 1
    if i in dp: return dp[i]
    
    dp[i] = solve(i//P-X)+solve(i//Q-Y)
    return dp[i]

N,P,Q,X,Y = map(int,input().split())

dp = dict()
print(solve(N))