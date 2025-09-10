# Plane Ticket Pricing
# Gold 3, DP, traceback

def traceback(n,x):
    for p,s in arr[i]:
        for j in range(s,-1,-1):
            if dp[i-1][n-j] == x-p*j:
                return n-j,x-p*j

N,W = map(int,input().split())
arr = []
for _ in range(W+1):
    ps = []
    k,*a = map(int,input().split())
    for i in range(k):
        ps.append((a[i],a[i+k]))
    arr.append(ps)

dp = [[-10**9]*(N+1) for _ in range(W+2)]
dp[-1][0] = 0
for i in range(W+1):
    for j in range(N+1):
        for p,s in arr[i]:
            k = min(s,N-j)
            dp[i][j+k] = max(dp[i][j+k],dp[i-1][j]+p*k)

x = max(dp[W])
n = dp[W].index(x)
print(x)

for _ in range(W):
    n,x = traceback(n,x)
    i -= 1
if n != 0:
    print(x//n)
else:
    m = 1000
    for p,s in arr[0]:
        if s == 0:
            m = min(m,p)
    print(m)