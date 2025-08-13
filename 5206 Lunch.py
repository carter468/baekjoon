# Lunch
# Gold 5, BFS

from collections import deque
import sys
input = sys.stdin.readline
INF = 10**9

def bfs(x,y):
    dist = [[INF]*W for _ in range(H)]
    dist[x][y] = 0
    q = deque([(x,y)])
    while q:
        x,y = q.popleft()
        for nx,ny in (x+1,y),(x-1,y),(x,y+1),(x,y-1):
            if 0 <= nx < H and 0 <= ny < W and dist[nx][ny] == INF and campus[nx][ny] != 'X':
                dist[nx][ny] = dist[x][y]+1
                if campus[nx][ny] != 'R': q.append((nx,ny))
    return dist

for t in range(int(input())):
    H,W = map(int,input().split())
    campus = [input() for _ in range(H)]

    S,M,R = [],[],[]
    for i in range(H):
        for j in range(W):
            if campus[i][j] == 'S': S.append((i,j))
            elif campus[i][j] == 'M': M.append((i,j))
            elif campus[i][j] == 'R': R.append((i,j))
    
    dist_M = [bfs(x,y) for x,y in M]
    dist_R = [bfs(x,y) for x,y in R]
    
    result = INF
    for i in range(len(M)):
        for j in range(len(R)):
            rx,ry = R[j]
            d = 0
            for x,y in S:
                d += dist_M[i][x][y]+dist_M[i][rx][ry]+dist_R[j][x][y]
            result = min(result,d)
    
    if result == INF: result = 'Impossible'
    print(f'Data Set {t+1}:',result,sep='\n')