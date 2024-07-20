# 칙령
# Gold 4, floyd-warshall

n = int(input())
d = int(input())
arr = [input() for _ in range(n)]

dist = [[10**9]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if arr[i][j] == 'Y':
            dist[i][j] = 1

for k in range(n):
    for i in range(n):
        for j in range(n):
            dist[i][j] = min(dist[i][j],dist[i][k]+dist[k][j])

result = 0
for i in range(n):
    for j in range(n):
        if i != j:
            result = max(result,dist[i][j])

if result == 10**9: print(-1)
else: print(result*d)