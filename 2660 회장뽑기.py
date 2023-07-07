# 회장뽑기
# Gold 5, floyd-warshall

import sys
input = sys.stdin.readline

n = int(input())
graph = [[51]*(n+1) for _ in range(n+1)]
while 1:
    a,b = map(int,input().split())
    if (a,b) == (-1,-1): break
    graph[a][b],graph[b][a] = 1,1
    
for i in range(1,n+1):
    graph[i][i] = 0

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            graph[i][j] = min(graph[i][j],graph[i][k]+graph[k][j])

result = [50,[]]
for i in range(1,n+1):
    t = max(graph[i][1:])
    if t < result[0]:
        result = [t,[i]]
    elif t == result[0]:
        result[1].append(i)

print(result[0],len(result[1]))
print(*result[1])