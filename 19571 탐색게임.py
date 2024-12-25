# 탐색 게임
# Gold 2, constructive

N = 100
arr = [[0]*N for _ in range(N)]
for i in range(N):
    arr[i][i] = N*N-i
x = 1
for i in range(N):
    for j in range(N):
        if i == N-2:
            if arr[i][N-1-j]: continue
            if j == 0:
                arr[i][j] = x
                x += 1
                arr[i][-1] = x
            else:
                arr[i][N-1-j] = x
        elif i == N-1:
            if arr[i][j]: continue
            arr[i][j] = x
        elif i%2 == 0:
            if arr[i][j]: continue
            arr[i][j] = x
        else:
            if arr[i][N-1-j]: continue
            arr[i][N-1-j] = x
        x += 1
for a in arr:
    print(*a)