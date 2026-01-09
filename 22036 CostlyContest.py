# Costly Contest
# Platinum 4, DP, greedy

_,_,K,T = map(int,input().split())
S = tuple(map(int,input().split()))
D = tuple(map(int,input().split()))

dp = [True]+[False]*T
for d in D:
    for i in range(T-d,-1,-1):
        dp[i+d] |= dp[i]

m = min(S)
t = max(i for i in range(T+1) if dp[i] and i*m <= T)

print(max(K,sum(1 for s in S if t*s <= T)))