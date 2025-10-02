# Graduation Guarantee
# Gold 2, DP, greedy, probability

N,K = map(int,input().split())
P = sorted(map(float,input().split()),reverse=True)

dp = [1]+[0]*(N*2)
result = 0
for i,p in enumerate(P):
    ndp = [0]*(N*2+1)
    psum = 0
    for j in range(-i-1,i+2):
        ndp[j] = dp[j-1]*p+dp[j+1]*(1-p)
        if j >= K: psum += ndp[j]
    dp = ndp
    result = max(result,psum)

print(result)