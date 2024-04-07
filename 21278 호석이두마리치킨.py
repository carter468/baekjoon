# 호석이 두 마리 치킨
# Gold 5, floyd-warshall, bruteforcing

n,m = map(int,input().split())
arr = [[999]*(n+1) for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    arr[a][b],arr[b][a] = 2,2

for k in range(1,n+1):
    arr[k][k] = 0
    for i in range(1,n+1):
        for j in range(1,n+1):
            arr[i][j] = min(arr[i][j],arr[i][k]+arr[k][j])

result = [0,0,99999]
for i in range(1,n+1):
    for j in range(i+1,n+1):
        x = 0
        for k in range(1,n+1):
            x += min(arr[i][k],arr[j][k])
        if x < result[2]: result = [i,j,x]
print(*result)