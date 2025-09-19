# 금오리
# Gold 3, geometry, DFS

R,L = map(int,input().split())
N,M = map(int,input().split())
lotus = [tuple(map(int,input().split())) for _ in range(N)]
duck = [tuple(map(int,input().split())) for _ in range(M)]

caught = [0]*M

for i in range(M):
    x,y = duck[i]
    if (x**2+y**2)**0.5+L >= R:
        caught[i] = 1

visited = [False]*N
for i in range(N):
    x,y,r = lotus[i]
    if not visited[i] and (x**2+y**2)**0.5+r >= R:
        visited[i] = True
        q = [i]
        while q:
            x = q.pop()
            x1,y1,r1 = lotus[x]
            for j in range(M):
                x2,y2 = duck[j]
                if (r1+L)**2 >= (x1-x2)**2+(y1-y2)**2:
                    caught[j] = 1
            
            for nx in range(N):
                x2,y2,r2 = lotus[nx]
                if not visited[nx] and (x1-x2)**2+(y1-y2)**2 <= (r1+r2)**2:
                    visited[nx] = True
                    q.append(nx)
print(sum(caught))