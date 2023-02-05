# 경쟁적 전염
# Gold 5, 너비 우선 탐색

import sys
input = sys.stdin.readline
dx = 1,-1,0,0
dy = 0,0,1,-1

N,K = map(int,input().split())
table = [tuple(map(int,input().split())) for _ in range(N)]
visit = [[0 for _ in range(N)] for _ in range(N)]
s,x,y = map(int,input().split())

nq = [(x-1,y-1)]
visit[x-1][y-1] = 1
result = []
if table[x-1][y-1]:
    result.append(table[x-1][y-1])
while s and not result:
    s -= 1
    q,nq = nq,[]
    while q:
        x,y = q.pop()
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if nx<0 or nx==N or ny<0 or ny==N or visit[nx][ny]:
                continue
            visit[nx][ny] = 1
            if table[nx][ny]:
                result.append(table[nx][ny])
            else:
                nq.append((nx,ny))

print(min(result) if result else 0)