# 데이트 약속
# Gold 1, DP, prefix sum

import sys
input = sys.stdin.readline

N,M = map(int,input().split())
arr = [(0,0)]+[tuple(map(int,input().split())) for _ in range(M)]+[(N+1,0)]

psum = [0] # i번째 저주데이까지 쭉 데이트 했을때 깎이는 총 애정도
dp = [0]+[-sys.maxsize]*(M+1) # i번째 저주데이 전날까지 데이트 했을때 최대 애정도
for i in range(1,M+2): # i번째 저주데이
    psum.append(psum[-1]+arr[i][1])
    for j in range(i): # j번째 저주데이 다음날부터 i번째 저주데이 전날까지 데이트
        d = arr[i][0]-arr[j][0]-1
        dp[i] = max(dp[i],dp[j]+d*(d+1)//2-(psum[i-1]-psum[j]))
print(dp[-1])