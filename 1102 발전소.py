# 발전소
# Platinum 5, DP, bitmask

# DFS 풀이 1048ms

def dfs(state,count):
    if count >= p: return 0
    if dp[state] != INF: return dp[state]
    for i in range(n):
        if state&1<<i != 0:
            for j in range(n):
                if state&1<<j == 0:
                    dp[state] = min(dp[state],dfs(state|1<<j,count+1)+arr[i][j])
    return dp[state]

INF = 10**9

n = int(input())
arr = [tuple(map(int,input().split())) for _ in range(n)]
yn = input()
p = int(input())

c,s = 0,0
for i in range(n):
    if yn[i] == 'Y':
        c += 1
        s += 1<<i

dp = [INF]*(1<<n)
result = dfs(s,c)
print(result if result != INF else -1)

# 그냥 DP 1668ms

INF = 10**9

n = int(input())
arr = [tuple(map(int,input().split())) for _ in range(n)]
yn = input()
p = int(input())

s = 0
for i in range(n):
    if yn[i] == 'Y':
        s += 1<<i

dp = [INF]*(1<<n)
dp[s] = 0
for i in range(1<<n):
    if dp[i] == INF: continue
    for j in range(n):
        if i&1<<j:
            for k in range(n):
                if i&1<<k==0:
                    dp[i|1<<k] = min(dp[i|1<<k],dp[i]+arr[j][k])

result = INF
for i in range(1<<n):
    if dp[i] != INF:
        count = 0
        for j in range(n):
            if i&1<<j: count += 1
        if count >= p:
            result = min(result,dp[i])
print(result if result != INF else -1)