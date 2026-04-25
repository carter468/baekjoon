# 녹색 옷 입은 애가 젤다지?
# Gold 4, dijkstra

import sys,heapq
input = sys.stdin.readline

t = 1
while (N:=int(input())):
    arr = [tuple(map(int,input().split())) for _ in range(N)]

    dist = [[10**9]*N for _ in range(N)]
    dist[0][0] = 0
    q = [(0,0,0)]
    while q:
        d,x,y = heapq.heappop(q)
        if d > dist[x][y]: continue
        for nx,ny in (x+1,y),(x-1,y),(x,y+1),(x,y-1):
            if 0 <= nx < N and 0 <= ny < N:
                nd = d+arr[nx][ny]
                if nd < dist[nx][ny]:
                    dist[nx][ny] = nd
                    heapq.heappush(q,(nd,nx,ny))
    print(f'Problem {t}: {arr[0][0]+dist[-1][-1]}')
    t += 1