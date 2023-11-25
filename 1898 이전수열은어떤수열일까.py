# 이전 수열은 어떤 수열일까
# Gold 2, greedy

import sys
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]

idx = [0]*(n+1)
check = [False]*(n+1)
for i in range(n):
    idx[arr[i]] = i

for i in range(n):
    k = arr[i]
    if k != 1 and idx[k] < idx[k-1] and check[k] == False and check[k-1] == False:
        check[k],check[k-1] = True,True
        arr[idx[k]],arr[idx[k-1]] = arr[idx[k-1]],arr[idx[k]]

for x in arr:
    print(x)