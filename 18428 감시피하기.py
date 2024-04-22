# 감시 피하기
# Gold 5, backtracking, bruteforcing

def check():
    for x,y in t:
        for dx,dy in (1,0),(-1,0),(0,1),(0,-1):
            nx,ny = x,y
            while 0 <= nx < n and 0 <= ny < n and arr[nx][ny] != 'O':
                if arr[nx][ny] == 'S': return
                nx += dx
                ny += dy
    print('YES')
    exit()

def solve(idx,count):
    if count == 3:
        return check()
    for i in range(idx+1,n*n):
        x,y = divmod(i,n)
        if arr[x][y] == 'X':
            arr[x][y] = 'O'
            solve(i,count+1)
            arr[x][y] = 'X'

n = int(input())
arr = [list(input().split()) for _ in range(n)]
t = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 'T': t.append((i,j))

solve(-1,0)
print('NO')