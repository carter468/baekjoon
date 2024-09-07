# 육각형 우리 속의 개미
# Gold 3, backtracking

def solve(x,y,c,d):
    global count
    if c == n: return
    for nd in (d+1,d-1):
        dx,dy = D[nd%6]
        nx,ny = x+dx,y+dy
        if visited[nx][ny]:
            if c == n-1: count += 1
        else:
            visited[nx][ny] = True
            solve(nx,ny,c+1,nd)
            visited[nx][ny] = False

D = [(0,1),(1,1),(1,-1),(0,-1),(-1,-1),(-1,1)]

n = int(input())

visited = [[False]*50 for _ in range(50)]
visited[0][0] = True
visited[0][1] = True
count = 0
solve(0,1,0,0)
print(count)
