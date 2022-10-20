# 세 친구

import sys
input = sys.stdin.readline

n,m = map(int,input().split())
graph = [[False for _ in range(n+1)] for _ in range(n+1)]
cnt = [0]*(n+1)
for _ in range(m):
    a,b = map(int,input().split())
    graph[a][b] = True
    graph[b][a] = True
    cnt[a] += 1
    cnt[b] += 1
answer = 20000
for i in range(1,n+1):
    for j in range(i+1,n+1):
        if graph[i][j] == False:
            continue
        for k in range(j+1,n+1):
            if graph[i][k] == False or graph[j][k] == False:
                continue
            answer = min(answer,cnt[i]+cnt[j]+cnt[k]-6)
if answer == 20000:
    print(-1)
else:
    print(answer)