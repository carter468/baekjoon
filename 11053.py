# 가장 긴 증가하는 부분수열

n = 12
seq = [1,2,3,4,10,20,10,11,12,30,20,50]
# n = int(input())
# seq = list(map(int,input().split()))
dp = [1]*n
max_len = 0
for i in range(n):
    for j in range(i):
        if seq[j] < seq[i]:         # i번째 수보다 작은 수의 부분수열길이들 중에 최대길이+1
            dp[i] = max(dp[i],dp[j]+1)
    max_len = max(dp[i],max_len)

print(dp)