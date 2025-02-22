# Campfire Riddle
# Gold 4, greedy

N = int(input())

k = 1
result = 0
while True:
    result += k*(k-1)//2
    x = k*(k+1)//2
    if x >= N: break
    k += 1
a = x-N
result -= a*(a-1)//2
print(result)

# DP
N = int(input())

dp = [0]+[10**9]*N
for i in range(1,N+1):
    for j in range(N,i-1,-1):
        dp[j] = min(dp[j],dp[j-i]+i*(i-1)//2)
print(dp[N])