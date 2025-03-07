# 임스의 땅따먹기
# Gold 3, bruteforcing, prefix sum

N = int(input())
arr = [tuple(map(int,input().split())) for _ in range(N)]
K = int(input())
d = [0]+sorted(map(int,input().split()),reverse=True)
for i in range(K):
    d[i+1] += d[i]

psum = [[0]*(N+1) for _ in range(N+1)]
count = [[0]*(N+1) for _ in range(N+1)]
for i in range(N):
    for j in range(N):
        psum[i][j] = arr[i][j]+psum[i-1][j]+psum[i][j-1]-psum[i-1][j-1]
        count[i][j] = (arr[i][j] == 0)+count[i-1][j]+count[i][j-1]-count[i-1][j-1]

result = 0
for i in range(N):
    for j in range(N):
        for k in range(N):
            a,b = i+k,j+k
            if a >= N or b >= N: break
            x = psum[a][b]-psum[i-1][b]-psum[a][j-1]+psum[i-1][j-1]
            y = count[a][b]-count[i-1][b]-count[a][j-1]+count[i-1][j-1]
            if y <= K:
                result = max(result,x+d[y])
print(result)