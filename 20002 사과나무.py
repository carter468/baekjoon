# 사과나무
# Gold 5, prefix sum

n = int(input())
arr = [[0]*(n+1)]+[[0]+list(map(int,input().split())) for _ in range(n)]

for i in range(n):
    for j in range(n):
        arr[i+1][j+1] += arr[i+1][j]+arr[i][j+1]-arr[i][j]

result = -1000
for i in range(n):
    for j in range(1,n+1-i):
        for k in range(1,n+1-i):
            result = max(result,arr[i+j][i+k]-arr[j-1][i+k]-arr[i+j][k-1]+arr[j-1][k-1])
print(result)
