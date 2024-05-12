# 끝나지 않는 파티
# Gold 5, floyd-warshall

n,m = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]

for k in range(n):
    for i in range(n):
        for j in range(n):
            arr[i][j] = min(arr[i][j],arr[i][k]+arr[k][j])

for _ in range(m):
    a,b,c = map(int,input().split())
    print('Enjoy other party' if arr[a-1][b-1] <= c else 'Stay here')