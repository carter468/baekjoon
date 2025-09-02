# 주사위 굴리기 2
# Gold 3, implementation, simulation, DFS

D = (0,1),(1,0),(0,-1),(-1,0)

def roll():
    if d == 0:
        return p[3],p[1],p[0],p[5],p[4],p[2]
    elif d == 1:
        return p[1],p[5],p[2],p[3],p[0],p[4]
    elif d == 2:
        return p[2],p[1],p[5],p[0],p[4],p[3]
    elif d == 3:
        return p[4],p[0],p[2],p[3],p[5],p[1]

N,M,K = map(int,input().split())
arr = [tuple(map(int,input().split())) for _ in range(N)]

score = [[0]*M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if score[i][j] == 0:
            visited = {(i,j)}
            q = [(i,j)]
            while q:
                x,y = q.pop()
                for nx,ny in (x+1,y),(x-1,y),(x,y+1),(x,y-1):
                    if 0 <= nx < N and 0 <= ny < M and (nx,ny) not in visited and arr[nx][ny] == arr[x][y]:
                        visited.add((nx,ny))
                        q.append((nx,ny))
            c = len(visited)
            for x,y in visited:
                score[x][y] = arr[x][y]*c

p = (1,2,3,4,5,6) 
ans,d,x,y = 0,0,0,0
for _ in range(K):
    dx,dy = D[d]
    nx,ny = x+dx,y+dy
    if 0 <= x+dx < N and 0 <= y+dy < M:
        x,y = x+dx,y+dy
    else:
        x,y = x-dx,y-dy
        d = (d+2)%4
    p = roll()
    if p[5] > arr[x][y]: d = (d+1)%4
    elif p[5] < arr[x][y]: d = (d-1)%4
    ans += score[x][y]
print(ans)