# 정사각형의 개수
# Gold 5, math

MOD = 10**9+7

N,K = map(int,input().split())

result = 0
k = K
for i in range(1,N+1):
    x = max(0,N-i-1)
    result = (result+((N-i+1)**2+(x+x%2)*(x//2+1)*2)*k)%MOD
    k = k*K%MOD
print(result)