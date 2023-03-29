# ABC
# Gold 1, DP

def solve(i,a,b,p):
    if i == n:
        if p == k:
            return 1
        else:
            return 0
        
    if dp[i][a][b][p]:
        return 0
    
    dp[i][a][b][p] = 1
    ans[i] = 'A'
    if solve(i+1,a+1,b,p):
        return 1
    ans[i] = 'B'
    if solve(i+1,a,b+1,p+a):
        return 1
    ans[i] = 'C'
    if solve(i+1,a,b,p+a+b):
        return 1
    
    return 0

n,k = map(int,input().split())
dp = [[[[0]*435 for _ in range(n)] for _ in range(n)] for _ in range(n)]
ans = ['']*n

print(''.join(ans) if solve(0,0,0,0) else -1)