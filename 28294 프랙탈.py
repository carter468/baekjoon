# 프랙탈
# Gold 3, exponentiation by squaring

M = 10**9+7
N,a = map(int,input().split())

x = pow(N,a,M)
y = pow(N-1,a,M)
print((x*N+N*(N-2)*(x-y))%M)