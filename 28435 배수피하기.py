# 배수 피하기
# Gold 2, math, combinatorics

M = 10**9+7

n,k = map(int,input().split())
count = [0]*k
for a in map(int,input().split()):
    count[a%k] += 1

result = count[0]+1
for i in range(1,k//2+1):
    if i*2 == k:
        result = result*(count[i]+1)%M
    else:
        result = result*(2**count[i]+2**count[k-i]-1)%M

print((result-n-1)%M)