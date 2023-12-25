# 그래프 변환
# Gold 2, DP, math

MOD = 10**9+7

n,k = map(int,input().split())

if k == 0: print(n)
else:
    a = (n-2)*2
    b = n*(n-1)//2
    for _ in range(k-1):
        b = (b*a//2)%MOD
        a = (a-1)*2
    print(b)