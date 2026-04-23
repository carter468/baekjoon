# 파티로 가는 길
# Platinum 5, BFS, constructive, implementation

from collections import deque
import sys
input = sys.stdin.readline
D = (0,1),(1,0),(0,-1),(-1,0)

def solve1():
    N,M = map(int,input().split())
    A = [input() for _ in range(N)]
    q = deque([(0,0)])
    visited = [[-1]*M for _ in range(N)]
    visited[0][0] = 0
    while q:
        x,y = q.popleft()
        if (x,y) == (N-1,M-1): break
        for nx,ny in (x+1,y),(x-1,y),(x,y+1),(x,y-1):
            if 0 <= nx < N and 0 <= ny < M and A[nx][ny] == '.' and visited[nx][ny] == -1:
                visited[nx][ny] = visited[x][y]+1
                q.append((nx,ny))
    x,y = N-1,M-1
    path = [(x,y)]
    while True:
        if (x,y) == (0,0): break
        for nx,ny in (x+1,y),(x-1,y),(x,y+1),(x,y-1):
            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == visited[x][y]-1:
                x,y = nx,ny
                path.append((x,y))
                break
        
    path.reverse()
    result = []
    x,y = 0,0
    d = 0 # 0:오, 1:아, 2: 왼, 3:위
    for nx,ny in path[1:]:
        for nd,a in ((d,1),((d+1)%4,2),((d-1)%4,3)): # 1:직진, 2:우회전, 3: 좌회전
            dx,dy = D[nd]
            if (x+dx,y+dy) == (nx,ny):
                result.append(a)
                d = nd
                x,y = nx,ny
                break
    dist = len(result)
    edge = []
    node = 1
    for a in result:
        for i in range(a):
            edge.append((node,node+i+1))
        node += a
    while node < dist*3:
        edge.append((node,node+1))
        node += 1
    print(dist)
    for u,v in edge:
        print(u,v)

def solve2():
    dic = {0:'R',1:'D',2:'L',3:'U'}
    dist = int(input())
    N = dist*3
    graph = [[] for _ in range(N+1)]
    for _ in range(N-1):
        u,v = map(int,input().split())
        graph[u].append(v)
        graph[v].append(u)
    result = []
    d = 0
    node = 1
    p = 0
    while len(result) < dist:
        x = len(graph[node])
        if node != 1: x -= 1
        if x == 2: d = (d+1)%4
        elif x == 3: d = (d-1)%4
        result.append(dic[d])
        for nx in graph[node]:
            if nx != p and len(graph[nx]) > 1:
                p = node
                node = nx
                break
    print(''.join(result))

T = int(input())
if T == 1: solve1()
else: solve2()