# 무기 공학
# Gold 4, backtracking

def solve(a,c):
    global result
    result = max(result,c)
    if a == n*m: return
    solve(a+1,c)
    x,y = divmod(a,m)
    if x+1 < n and y+1 < m:
        if empty[x][y] and empty[x][y+1] and empty[x+1][y+1]:
            empty[x][y],empty[x][y+1],empty[x+1][y+1] = False,False,False
            solve(a+2,c+arr[x][y]+arr[x][y+1]*2+arr[x+1][y+1])
            empty[x][y],empty[x][y+1],empty[x+1][y+1] = True,True,True
        if empty[x][y] and empty[x+1][y] and empty[x+1][y+1]:
            empty[x][y],empty[x+1][y],empty[x+1][y+1] = False,False,False
            solve(a+1,c+arr[x][y]+arr[x+1][y]*2+arr[x+1][y+1])
            empty[x][y],empty[x+1][y],empty[x+1][y+1] = True,True,True
        if empty[x][y] and empty[x][y+1] and empty[x+1][y]:
             empty[x][y],empty[x][y+1],empty[x+1][y] = False,False,False
             solve(a+2,c+arr[x][y]*2+arr[x][y+1]+arr[x+1][y])
             empty[x][y],empty[x][y+1],empty[x+1][y] = True,True,True
    if x+1 < n and y > 0 and empty[x][y] and empty[x+1][y] and empty[x+1][y-1]:
            empty[x][y],empty[x+1][y],empty[x+1][y-1] = False,False,False
            solve(a+1,c+arr[x][y]+arr[x+1][y]*2+arr[x+1][y-1])
            empty[x][y],empty[x+1][y],empty[x+1][y-1] = True,True,True

n,m = map(int,input().split())
arr = [tuple(map(int,input().split())) for _ in range(n)]

empty = [[True]*m for _ in range(n)]
result = 0
solve(0,0)
print(result)