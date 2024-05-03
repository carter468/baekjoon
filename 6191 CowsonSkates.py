# Cows on Skates
# Gold 5, DFS

def dfs(x,y):
    if (x,y) == (r-1,c-1):
        for a,b in result:
            print(a+1,b+1)
        exit()
    for nx,ny in (x+1,y),(x-1,y),(x,y+1),(x,y-1):
        if 0 <= nx < r and 0 <= ny < c and arr[nx][ny] == '.':
            arr[nx][ny] = '*'
            result.append((nx,ny))
            dfs(nx,ny)
            result.pop()

r,c = map(int,input().split())
arr = [list(input()) for _ in range(r)]

result = [(0,0)]
arr[0][0] = '*'
dfs(0,0)