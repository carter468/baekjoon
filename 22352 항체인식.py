# 항체 인식
# Gold 5, 너비 우선 탐색

import sys
input = sys.stdin.readline
dx=1,-1,0,0
dy=0,0,1,-1

def spread(i,j,pt,ct):
    q = [(i,j)]
    while q:
        x,y = q.pop()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx<0 or nx==N or ny<0 or ny==M or visit[nx][ny] or prev[nx][ny]!=pt:continue
            if curr[nx][ny]!=ct:
                return False
            visit[nx][ny] = 1
            q.append((nx,ny))
    return True

def solve():
    count = 0
    for i in range(N):
        for j in range(M):
            if visit[i][j] or prev[i][j]==curr[i][j]:continue
            if not spread(i,j,prev[i][j],curr[i][j]):
                return 'NO'
            count += 1
    return 'YES' if count<2 else 'NO'

N,M = map(int,input().split())
prev,curr = [],[]
for i in range(N):
    prev.append(tuple(map(int,input().split())))
for i in range(N):
    curr.append(tuple(map(int,input().split())))

visit = [[0]*M for _ in range(N)]
print(solve())