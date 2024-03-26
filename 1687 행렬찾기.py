# 행렬 찾기
# Gold 3, bruteforcing, prefix sum

n,m = map(int,input().split())
arr = [tuple(map(int,input())) for _ in range(n)]

psum = [[0]*(m+1) for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,m+1):
        psum[i][j] = psum[i-1][j]+psum[i][j-1]-psum[i-1][j-1]+arr[i-1][j-1]

result = 0
for i in range(1,m+1):
    for j in range(1,m+1):
        k = 1
        a = 0
        for l in range(1,n+1):
            b = psum[l][j]-psum[l][i-1]
            if a == b: result = max(result,(l-k+1)*(j-i+1))
            elif b > a: k = l+1
            a = b
print(result)