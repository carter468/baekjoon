# 얼음 미로
# Gold 2, dijkstra

import heapq
import sys
input = sys.stdin.readline
INF = sys.maxsize

def escape():
    q = []
    heapq.heappush(q,(0,(s1,s2)))
    distance[s1][s2] = 0
    while q:
        dist,loca = heapq.heappop(q)
        x,y = loca
        if dist>distance[x][y]: continue
        for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
            nx,ny,t = x+dx,y+dy,0
            while 0<=nx<H and 0<=ny<W and maze[nx][ny]!='H':
                if maze[nx][ny].isdigit():
                    t += int(maze[nx][ny])
                if maze[nx][ny]=='R':
                    nx -= dx
                    ny -= dy
                    break
                if maze[nx][ny]=='E':
                    break
                nx += dx
                ny += dy
            else:
                continue
            if dist+t<distance[nx][ny]:
                distance[nx][ny] = dist+t
                if maze[nx+dx][ny+dy]=='R':
                    heapq.heappush(q,(distance[nx][ny],(nx,ny)))

W,H = map(int,input().split())
distance = [[INF]*W for _ in range(H)]
maze = []
for i in range(H):
    maze.append(input())
    for j in range(W):
        if maze[i][j] == 'T':
            s1,s2 = i,j
        elif maze[i][j] == 'E':
            e1,e2 = i,j

escape()
print(-1 if distance[e1][e2]==INF else distance[e1][e2])