# 보이저 1호
# Gold 5, implementation

D = ((-1,0),(0,1),(1,0),(0,-1)) 
INF = 10**9
n,m = map(int,input().split())
grid = [input() for _ in range(n)]
x,y = map(int,input().split())
x,y = x-1,y-1

result = []
for i in range(4):
    d = i
    nx,ny = x,y
    count = 0
    visited = [[[False]*4 for _ in range(m)] for _ in range(n)]
    while 0 <= nx < n and 0 <= ny < m and grid[nx][ny] != 'C':
        if visited[nx][ny][d]:
            count = INF
            break
        count += 1
        visited[nx][ny][d] = True
        if grid[nx][ny] == '/':
            if d <= 1: d = 1-d
            else: d = 5-d
        elif grid[nx][ny] == '\\':
            d = 3-d
        nx += D[d][0]
        ny += D[d][1]
    result.append((count,i))
result.sort(key=lambda x:(-x[0],x[1]))
print('URDL'[result[0][1]])
print(result[0][0] if result[0][0] != INF else 'Voyager')
