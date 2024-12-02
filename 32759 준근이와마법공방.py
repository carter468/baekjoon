# 준근이와 마법 공방
# Gold 4, ad hoc, simulation

MOD = 10**9+7

N,M = map(int,input().split())
arr = sorted(map(int,input().split()))

a,b = arr[-1],arr[-2]
for _ in range(N):
    result = a+b
    if a > 0 and b > 0:
        a,b = (a+b)%MOD,a%MOD
    else:
        _,b,a = sorted([a,b,a+b])

print(result%(10**9+7))