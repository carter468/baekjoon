# 두 덱
# Gold 5, DP

N,K = map(int,input().split())
A = list(map(int,input().split()))+[0]
B = list(map(int,input().split()))+[0]

DP_A = [[sum(A)]*(K+1) for _ in range(K+1)]
DP_B = [[sum(B)]*(K+1) for _ in range(K+1)]
for i in range(1,K+1): # i개 제거
    for j in range(i+1): # 앞에서 j개 제거
        k = i-j   # 뒤에서 k개 제거
        if j == 0:
            DP_A[i][j] = DP_A[i-1][j]-A[N-k]
            DP_B[i][j] = DP_B[i-1][j]-B[N-k]
        else:
            DP_A[i][j] = min(DP_A[i-1][j]-A[N-k],DP_A[i-1][j-1]-A[j-1])
            DP_B[i][j] = min(DP_B[i-1][j]-B[N-k],DP_B[i-1][j-1]-B[j-1])

result = 10**15
for i in range(K+1):
    result = min(result,max(min(DP_A[i]),min(DP_B[K-i])))
print(result)