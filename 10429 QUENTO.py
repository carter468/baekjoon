# QUENTO
# Gold 4, backtracking

def move(x,y,total,count):
    if count == m*2-1:
        if eval(total) == n:
            print(1)
            for r in result:
                print(*r)
            exit()
        return
    
    for nx,ny in (x+1,y),(x-1,y),(x,y+1),(x,y-1):
        if 0 <= nx < 3 and 0 <= ny < 3 and not visited[nx][ny]:
            visited[nx][ny] = True
            result.append((nx,ny))
            move(nx,ny,total+arr[nx][ny],count+1)
            visited[nx][ny] = False
            result.pop()

n,m = map(int,input().split())
arr = [input() for _ in range(3)]

visited = [[False]*3 for _ in range(3)]
result = []
for x,y in (0,0),(0,2),(1,1),(2,0),(2,2):
    visited[x][y] = True
    result.append((x,y))
    move(x,y,arr[x][y],1)
    visited[x][y] = False
    result.pop()
print(0)