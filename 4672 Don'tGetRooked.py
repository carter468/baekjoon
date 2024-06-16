# Don't Get Rooked
# Gold 5, bruteforcing, backtracking

def solve(idx,count,board):
    global result
    result = max(result,count)

    if idx == n*n: return

    solve(idx+1,count,board)
    x,y = divmod(idx,n)
    if board[x][y] == '.':
        nboard = [board[i][:] for i in range(n)]
        for dx,dy in (1,0),(-1,0),(0,1),(0,-1):
            nx,ny = x,y
            while 0 <= nx < n and 0 <= ny < n and board[nx][ny] != 'X':
                nboard[nx][ny] = 'O'
                nx += dx
                ny += dy
        solve(idx+1,count+1,nboard)

while n:=int(input()):
    arr = [list(input()) for _ in range(n)]
    result = 0
    solve(0,0,arr)
    print(result)