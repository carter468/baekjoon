# 체스판 다시 칠하기 2
# Gold 5, prefix sum

n,m,k = map(int,input().split())
arr = [input() for _ in range(n)]

c = [[0]*(m+1) for _ in range(n+1)]
for i in range(n):
    for j in range(m):
        c[i+1][j+1] += c[i][j+1]+c[i+1][j]-c[i][j]+(arr[i][j] == 'BW'[(i+j)%2])

x = result = k*k
for i in range(k,n+1):
    for j in range(k,m+1):
        a = c[i][j]-c[i-k][j]-c[i][j-k]+c[i-k][j-k]
        result = min(result,a,x-a)
print(result)