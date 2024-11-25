# The Lazy Cow
# Gold 4, prefix sum

N,K = map(int,input().split())
arr = [tuple(map(int,input().split())) for _ in range(N)]

n = N*2-1
board = [[0]*(n+1) for _ in range(n+1)]
for i in range(n):
    c = abs(N-1-i)
    for j in range(i+1):
        a,b = i-j,j
        if 0 <= a < N and 0 <= b < N:
            board[i][c] = arr[a][b]
            c += 2

for i in range(n):
    for j in range(n):
        board[i][j] += board[i-1][j]+board[i][j-1]-board[i-1][j-1]

result = 0
for i in range(n):
    for j in range(n):
        if (i+j+N)%2 == 0: continue
        x1,y1 = max(0,i-K),max(0,j-K)
        x2,y2 = min(n-1,i+K),min(n-1,j+K)
        result = max(result,board[x2][y2]-board[x2][y1-1]-board[x1-1][y2]+board[x1-1][y1-1])

print(result)