# Trokut
# Gold 4, implementation, recursive

def solve(s,x,y):
    if s == 1:
        arr[x-2][y-3] = arr[x-1][y-4] = '/'
        arr[x-2][y-2] = arr[x-1][y-1] = '\\'
        arr[x-1][y-3] = arr[x-1][y-2] = '_'
        return

    for dx,dy in (0,0),(1<<s-1,1<<s-1),(0,1<<s):
        solve(s-1,x-dx,y-dy)

N = int(input())

M = 1<<N
arr = [['.']*(M+i+1) for i in range(M)]
solve(N,M,M*2)
for i in range(M):
    print(''.join(arr[i]))