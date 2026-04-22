# 爆発の連鎖
# Gold 5, DFS

import sys
input = sys.stdin.readline

while True:
    _,_,N,D,B = map(int,input().split())
    if N == 0: break

    bomb = [tuple(map(int,input().split())) for _ in range(N)]
    q = [bomb[B-1]]
    while q:
        x,y = q.pop()
        nbomb = []
        for nx,ny in bomb:
            if x != nx and y != ny:
                nbomb.append((nx,ny))
            elif abs(x-nx)+abs(y-ny) > D:
                nbomb.append((nx,ny))
            else:
                q.append((nx,ny))
        bomb = nbomb
    print(N-len(bomb))