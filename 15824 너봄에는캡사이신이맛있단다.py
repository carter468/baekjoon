# 너 봄에는 캡사이신이 맛있단다
# Gold 2, math, combinatorics

MOD = 10**9+7

N = int(input())
A = sorted(map(int,input().split()))

result = 0
p = 1
for i,a in enumerate(A,1):
    result = (result+a*(p-(pow(2,N-i,MOD)-1))-a)%MOD
    p = p*2%MOD

print(result)