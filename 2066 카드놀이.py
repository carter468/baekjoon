# 카드놀이
# Gold 1, DP

def solve(x):
    if x not in dp:
        dp[x] = 0
        for i in range(9):
            if x[i] == 3: continue
            for j in range(i+1,9):
                if x[j] < 3 and A[i][x[i]+1][0] == A[j][x[j]+1][0]:
                    nx = list(x)                
                    nx[i] += 1
                    nx[j] += 1
                    dp[x] += solve(tuple(nx))

    c = 0
    for i in range(9):
        if x[i] == -1: continue
        for j in range(i+1,9):
            if x[j] != -1 and A[i][x[i]][0] == A[j][x[j]][0]: c += 1

    if c == 0: return dp[x]
    return dp[x]/c

A = [input().split() for _ in range(9)]

dp = {(3,3,3,3,3,3,3,3,3):1}
print(solve((-1,-1,-1,-1,-1,-1,-1,-1,-1)))