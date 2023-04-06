# 열차정렬
# Gold 1, DP

import sys
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]

result = 0
l1,l2 = [1]*n,[1]*n
for i in range(n-1,-1,-1):
    for j in range(i+1,n):
        if arr[i] > arr[j]:
            l1[i] = max(l1[i],l1[j]+1)
        else:
            l2[i] = max(l2[i],l2[j]+1)
    result = max(result,l1[i]+l2[i]-1)

print(result)