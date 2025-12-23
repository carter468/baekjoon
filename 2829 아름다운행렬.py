# 아름다운 행렬
# Gold 3, bruteforcing, prefix sum

N = int(input())
arr = [tuple(map(int,input().split())) for _ in range(N)]

sum1 = [[0]*(N+1) for _ in range(N+1)]
sum2 = [[0]*(N+2) for _ in range(N+2)]
for i in range(N):
    for j in range(N):
        sum1[i+1][j+1] += sum1[i][j]+arr[i][j]
for i in range(N):
    for j in range(N):
        sum2[i+1][j+1] += sum2[i][j+2]+arr[i][j]

result = 0
for i in range(1,N+1):
    for j in range(1,N+1):
        for k in range(1,N+1):
            a,b = i+k,j+k
            if a > N or b > N: break
            x = sum1[a][b]-sum1[i-1][j-1]
            y = sum2[a][j]-sum2[i-1][b+1]
            result = max(result,x-y)
print(result)