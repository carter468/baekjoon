# 서강그라운드
# Gold 4, floyd-warshall

n,m,r = map(int,input().split())
arr = tuple(map(int,input().split()))
dist = [[16]*n for _ in range(n)]
for _ in range(r):
    a,b,c = map(int,input().split())
    dist[a-1][b-1] = c
    dist[b-1][a-1] = c

for k in range(n):
    for i in range(n):
        for j in range(n):
            dist[i][j] = min(dist[i][j],dist[i][k]+dist[k][j])

result = 0
for i in range(n):
    temp = arr[i]
    for j in range(n):
        if i != j and dist[i][j] <= m:
            temp += arr[j]
    result = max(result,temp)
print(result)