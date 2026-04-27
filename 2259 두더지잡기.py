# 두더지 잡기
# Gold 3, DP

import sys
input = sys.stdin.readline

N,S = map(int,input().split())
A = [(0,0,0)]+[tuple(map(int,input().split())) for _ in range(N)]
A.sort(key=lambda x:x[2])

S *= S
dp = [0]+[-N]*N
for i in range(1,N+1):
    x,y,t = A[i]
    for j in range(i):
        x1,y1,t1 = A[j]
        if (t1-t)**2*S >= (x-x1)**2+(y-y1)**2 and dp[i] < dp[j]+1:
            dp[i] = dp[j]+1
print(max(dp))