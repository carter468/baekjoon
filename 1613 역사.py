# 역사
# Gold 3, floyd-warshall

import sys
input = sys.stdin.readline

n,k = map(int,input().split())
arr = [[0]*(n+1) for _ in range(n+1)]
for _ in range(k):
    a,b = map(int,input().split())
    arr[a][b] = -1
    arr[b][a] = 1

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if arr[i][j] == 0 and arr[i][k] == arr[k][j]:
                arr[i][j] = arr[i][k]

for _ in range(int(input())):
    a,b = map(int,input().split())
    print(arr[a][b])