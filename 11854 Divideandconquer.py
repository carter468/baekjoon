# Divide and conquer
# Platinum 3, DP, binary search, prefix sum

import sys,bisect
input = sys.stdin.readline

N = int(input())
p,g,e = [0]*N,[0]*N,[0]*N
for i in range(N):
    p[i],g[i],e[i] = map(int,input().split())

arr = []
gps,eps = [0],[0]
for i in range(N):
    gps.append(gps[-1]+g[i])
    eps.append(eps[-1]+e[i])
    arr.append((eps[-1]-p[i],i))
arr.sort()

dp = [0]*(N+1)
for i in range(N-1,-1,-1):
    dp[i] = max(dp[i+1],arr[i][1])

result = 0
for i in range(N):
    target = eps[i]-p[i]
    j = bisect.bisect_left(arr,(target,0))
    if j < N:
        result = max(result,gps[dp[j]+1]-gps[i])
print(result)