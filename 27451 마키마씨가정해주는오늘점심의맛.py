# 마키마씨가 정해주는 오늘 점심의 맛
# Platinum 4, BFS, traceback

from collections import deque
import sys
input = sys.stdin.readline

N,M = map(int,input().split())
A,B,C = map(int,input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    s,e = map(int,input().split())
    graph[s].append(e)

visited = [[[None]*(N+1) for _ in range(N+1)] for _ in range(N+1)]
visited[A][B][C] = 1
q = deque([(A,B,C,0)])
while q:
    a,b,c,d = q.popleft()
    if a == b == c:
        print(a,d)
        pa,pb,pc = [],[],[]
        while (a,b,c) != (A,B,C):
            pa.append(a)
            pb.append(b)
            pc.append(c)
            a,b,c = visited[a][b][c]
        pa.append(A)
        pb.append(B)
        pc.append(C)
        print(*pa[::-1])
        print(*pb[::-1])
        print(*pc[::-1])
        break

    for na in graph[a]:
        for nb in graph[b]:
            for nc in graph[c]:
                if not visited[na][nb][nc]:
                    visited[na][nb][nc] = (a,b,c)
                    q.append((na,nb,nc,d+1))

else: print(-1)