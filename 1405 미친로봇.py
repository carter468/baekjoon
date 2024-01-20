# 미친 로봇
# Gold 4, backtracking, probability

def move(x,y,p,count):
    global result
    if count == n:
        result += p
        return
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if visited[nx][ny] == False:
            visited[nx][ny] = True
            move(nx,ny,p*arr[i],count+1)
            visited[nx][ny] = False

n,*arr = map(int,input().split())

dx = 1,-1,0,0
dy = 0,0,-1,1
result = 0
visited = [[False]*30 for _ in range(30)]
visited[0][0] = True
move(0,0,1,0)

print(result/(100**n))