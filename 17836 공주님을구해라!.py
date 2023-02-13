# 공주님을 구해라!
# Gold 5, 너비 우선 탐색

from collections import deque
import sys
input = sys.stdin.readline

def rescue():
    N,M,T = map(int,input().split())
    castle = [tuple(input().split()) for _ in range(N)]
    visit = [[-1]*M for _ in range(N)]
    withgram = 10001

    q = deque([(0,0)])
    visit[0][0] = 0
    while q:
        x,y = q.popleft()
        if visit[x][y] == T:
            return withgram if withgram<=T else 'Fail'
        for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
            nx,ny = x+dx,y+dy
            if nx<0 or nx==N or ny<0 or ny==M or visit[nx][ny]!=-1 or castle[nx][ny]=='1':
                continue
            if (nx,ny)==(N-1,M-1):
                return min(withgram,visit[x][y]+1)
            visit[nx][ny] = visit[x][y]+1
            if castle[nx][ny]=='2':
                withgram = N-1-nx+M-1-ny+visit[nx][ny]
            else:
                q.append((nx,ny))
    return withgram if withgram<=T else 'Fail'

print(rescue())