# 태상이의 훈련소 생활
# Gold 5, prefix sum, IMOS

import sys
input = sys.stdin.readline

n,m = map(int,input().split())
arr1 = tuple(map(int,input().split()))
arr2 = [0]*(n+1)
for _ in range(m):
    a,b,k = map(int,input().split())
    arr2[a-1] += k
    arr2[b] -= k

for i in range(n):
    arr2[i+1] += arr2[i]
    print(arr1[i]+arr2[i],end=' ')