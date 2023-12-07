# 발코딩
# Gold 3, DP

def recur(i,j):
    if (i,j) == (0,0): return
    if dp[i][j] == 1: recur(i-1,j)
    elif dp[i][j] == 2: recur(i,j-1)
    result.append(dp[i][j])

cy,gs,ans = input(),input(),input()

l1,l2 = len(cy),len(gs)
dp = [[0]*(l2+1) for _ in range(l1+1)]
dp[0][0] = 1
for i in range(l1+1):
    for j in range(l2+1):
        if dp[i][j] != 0:
            if i != l1 and ans[i+j] == cy[i]: dp[i+1][j] = 1
            if j != l2 and ans[i+j] == gs[j]: dp[i][j+1] = 2

result = []
recur(l1,l2)
print(''.join(map(str,result)))