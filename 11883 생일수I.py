# 생일수 I
# Gold 3, DP, greedy

M = 10**6+1

def count(x):
    a = dp[x][1]
    b = (x-a*3)//5
    c = min(a,b)
    return a+b-c*2

dp = [(M,0)]*M
dp[0] = (0,0)
for i in range(1,M):
    if i-3 >= 0 and dp[i-3][0] != M:
        d = count(i-3)
        if d < dp[i][0]:
            dp[i] = (d+1,dp[i-3][1]+1)
    if i-5 >= 0 and dp[i-5][0] != M:
        d = count(i-5)
        if d < dp[i][0]:
            dp[i] = (d+1,dp[i-5][1])
    if i-8 >= 0 and dp[i-8][0] != M:
        d = count(i-8)
        if d < dp[i][0]:
            dp[i] = (d+1,dp[i-8][1]+1)
    
for _ in range(int(input())):
    n = int(input())
    if dp[n][0] == M:
        print(-1)
    else:
        a = dp[n][1]
        b = (n-a*3)//5
        c = min(a,b)
        print('3'*(a-c)+'5'*(b-c)+'8'*c)