# Taking Metro (Small)
# Platinum 5, dijkstra

import sys,heapq
input = sys.stdin.readline
INF = 10**9

def dijkstra(x1,y1,x2,y2):
    dist = {(x1,y1,True):0}
    q = [(0,x1,y1,True)]
    while q:
        d,x,y,tr = heapq.heappop(q)
        if d > dist.get((x,y),INF): continue

        for nx,ny,t in tunnel.get((x,y),[]):
            nd = d+t
            if nd < dist.get((nx,ny,True),INF):
                dist[(nx,ny,True)] = nd
                heapq.heappush(q,(nd,nx,ny,True))

        if tr: d += lines[x][0]

        for ny in (y-1,y+1):
            if 0 < ny <= len(lines[x]):
                nd = d+lines[x][min(y,ny)]
                if nd < dist.get((x,ny,False),INF):
                    dist[(x,ny,False)] = nd
                    heapq.heappush(q,(nd,x,ny,False))

    result = min(dist.get((x2,y2,True),INF),dist.get((x2,y2,False),INF))
    return result if result != INF else -1

for tc in range(int(input())):
    input()
    lines = [[]]
    for _ in range(int(input())):
        _,w = map(int,input().split())
        lines.append([w]+list(map(int,input().split())))
    
    tunnel = dict()
    for _ in range(int(input())):
        m1,s1,m2,s2,t = map(int,input().split())
        if (m1,s1) in tunnel:
            tunnel[(m1,s1)].append((m2,s2,t))
        else:
            tunnel[(m1,s1)] = [(m2,s2,t)]
        if (m2,s2) in tunnel:
            tunnel[(m2,s2)].append((m1,s1,t))
        else:
            tunnel[(m2,s2)] = [(m1,s1,t)]

    print(f'Case #{tc+1}:')
    for _ in range(int(input())):
        x1,y1,x2,y2 = map(int,input().split())
        print(dijkstra(x1,y1,x2,y2))