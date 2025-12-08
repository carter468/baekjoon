# 포닉스와 지구 정복
# Gold 1, DFS, invariant

import sys
input = sys.stdin.readline

N,M,K = map(int,input().split())
A = [tuple(map(int,input().split())) for _ in range(N)]
B = [tuple(map(int,input().split())) for _ in range(N)]

visited = [[False]*M for _ in range(N)]
for _ in range(K):
    x,y = map(int,input().split())
    x,y = x-1,y-1
    if A[x][y] != B[x][y]: exit(print('No'))
    visited[x][y] = True

for i in range(N):
    for j in range(M):
        if not visited[i][j]:
            visited[i][j] = True
            a,b = 0,0
            q = [(i,j)]
            while q:
                x,y = q.pop()
                if (x+y)%2 == 0:
                    a += A[x][y]-B[x][y]
                else:
                    b += A[x][y]-B[x][y]
                for nx,ny in (x+1,y),(x-1,y),(x,y+1),(x,y-1):
                    if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                        visited[nx][ny] = True
                        q.append((nx,ny))
            if a != b: exit(print('No'))
print('Yes')