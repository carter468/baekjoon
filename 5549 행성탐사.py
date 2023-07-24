# 행성 탐사
# Gold 5, prefix sum

import sys
input = sys.stdin.readline

m,n = map(int,input().split())
k = int(input())
arr = [input() for _ in range(m)]

jun = [[0]*(n+1) for _ in range(m+1)]
oce = [[0]*(n+1) for _ in range(m+1)]
ice = [[0]*(n+1) for _ in range(m+1)]
for i in range(1,m+1):
    for j in range(1,n+1):
        jun[i][j] = jun[i-1][j]+jun[i][j-1]-jun[i-1][j-1]
        oce[i][j] = oce[i-1][j]+oce[i][j-1]-oce[i-1][j-1]
        ice[i][j] = ice[i-1][j]+ice[i][j-1]-ice[i-1][j-1]
        if arr[i-1][j-1] == 'J': jun[i][j] += 1
        if arr[i-1][j-1] == 'O': oce[i][j] += 1
        if arr[i-1][j-1] == 'I': ice[i][j] += 1

for _ in range(k):
    a,b,c,d = map(int,input().split())
    print(jun[c][d]-jun[c][b-1]-jun[a-1][d]+jun[a-1][b-1],oce[c][d]-oce[c][b-1]-oce[a-1][d]+oce[a-1][b-1],ice[c][d]-ice[c][b-1]-ice[a-1][d]+ice[a-1][b-1])