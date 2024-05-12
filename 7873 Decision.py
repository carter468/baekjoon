# Decision
# Gold 5, BFS, implementation

def check(k):
    dx,dy,c = D[k]
    nx,ny = x+dx,y+dy
    if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] in c and not visited[nx][ny]:
        visited[nx][ny] = True
        q.append((nx,ny))

D = [(-1,0,'BEF'),(1,0,'CDF'),(0,-1,'DEF'),(0,1,'BCF')]

for _ in range(int(input())):
    n,m = map(int,input().split())
    arr = [input() for _ in range(n)]
    count = 0
    visited = [[False]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and arr[i][j] != 'A':
                q = [(i,j)]
                visited[i][j] = True
                count += 1
                while q:
                    x,y = q.pop()
                    if arr[x][y] == 'B':
                        for k in (1,2):
                            check(k)
                    elif arr[x][y] == 'C':
                        for k in (0,2):
                            check(k)
                    elif arr[x][y] == 'D':
                        for k in (0,3):
                            check(k)
                    elif arr[x][y] == 'E':
                        for k in (1,3):
                            check(k)
                    elif arr[x][y] == 'F':
                        for k in range(4):
                            check(k)
    print(count)