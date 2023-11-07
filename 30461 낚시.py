# 낚시
# Gold 4, prefix sum

import sys
input = sys.stdin.readline

n,m,q = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]

for j in range(m):
    for i in range(n-1):
        arr[i+1][j] += arr[i][j]

for i in range(n-1):
    for j in range(m-1):
        arr[i+1][j+1] += arr[i][j]

for _ in range(q):
    a,b = map(int,input().split())
    print(arr[a-1][b-1])