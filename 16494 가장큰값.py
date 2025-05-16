# 가장 큰 값
# Gold 5, DP, bruteforcing, prefix sum

import itertools

N,M = map(int,input().split())

arr = list(map(int,input().split()))+[0]
for i in range(N-1):
    arr[i+1] += arr[i]

dp = [[-9999]*N for _ in range(N)]
for i in range(N):
    for j in range(i,N):
        for a in range(i,j+1):
            for b in range(a,j+1):
                dp[i][j] = max(dp[i][j],arr[b]-arr[a-1])

result = -9999
for c in itertools.combinations(range(1,N),M-1):
    c = [0]+list(c)+[N]

    t = 0
    for i in range(M):
        t += dp[c[i]][c[i+1]-1]
    result = max(result,t)
print(result)