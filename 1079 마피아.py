# 마피아
# Gold 2, bruteforcing

def solve(g,day,dead):
    global result
    result = max(result,day)
    m = -999
    for i in range(n):
        if i not in dead and g[i] > m:
            m = g[i]
            idx = i
    if idx == x: return
    dead.append(idx)
    for i in range(n):
        if i != x and i not in dead:
            ng = g[::]
            for j in range(n):
                ng[j] += arr[i][j]
            solve(ng,day+1,dead+[i])

n = int(input())
g = list(map(int,input().split()))
arr = [tuple(map(int,input().split())) for _ in range(n)]
x = int(input())

result = 0
if n%2 == 0:
    for i in range(n):
        if i != x:
            ng = g[::]
            for j in range(n):
                ng[j] += arr[i][j]
            solve(ng,1,[i])
else:
    solve(g,0,[])
print(result)
