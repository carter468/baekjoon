# 축구 대회
# Platinum 5

# bruteforcing, greedy

import sys
input = sys.stdin.readline

N = int(input())
arr = []
for i in range(N):
    arr.append([*map(int,input().split()),i])

A = sorted(arr,key=lambda x:-x[0])[:11]
B = sorted(arr,key=lambda x:-x[1])[:11]
C = sorted(arr,key=lambda x:-x[2])[:11]
D = sorted(arr,key=lambda x:-x[3])[:11]
E = sorted(arr,key=lambda x:-max(x[0],x[1],x[2]))[:11]

result = 0
for a,_,_,_,i in A:
    for _,b,_,_,j in B:
        for _,_,c,_,k in C:
            for _,_,_,d,l in D:
                s = {i,j,k,l}
                if len(s) != 4: continue
                idx = 0
                count = 0
                score = a+b+c+d
                while count < 7:
                    if E[idx][4] not in s:
                        score += max(E[idx][:3])
                        count += 1
                    idx += 1
                result = max(result,score)
print(result)

# DP

import sys
input = sys.stdin.readline

dp = [[-1]*16 for _ in range(12)]
dp[0][0] = 0
for _ in range(int(input())):
    arr = tuple(map(int,input().split()))
    ndp = [dp[i][:] for i in range(12)]
    for i in range(11):
        for j in range(16):
            for k in range(4):
                if dp[i][j] == -1 or (j >= 8 and k == 3): continue
                ndp[i+1][j|1<<k] = max(ndp[i+1][j|1<<k],dp[i][j]+arr[k])
    dp = [ndp[i][:] for i in range(12)]
print(dp[-1][-1])