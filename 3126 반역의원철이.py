# 반역의 원철이
# Gold 3, bruteforcing, prefix sum

M = (0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1),(1,0),(1,1)

Xm,Ym,Xb,Yb = map(int,input().split())
N = int(input())
S = list(input())

count = [[0]*8 for _ in range(N+1)]
k = 0
for i in range(N):
    k += int(S[i])
    k %= 8
    S[i] = k
    count[i][k] = 1
    for j in range(8):
        count[i][j] += count[i-1][j]

x,y = Xm,Ym
result = 10**9
for i in range(N):
    arr = [count[-2][j]-count[i-1][j] for j in range(8)]
    for j in range(8):
        nx,ny = x,y
        for k in range(8):
            dx,dy = M[(j+k)%8]
            nx += dx*arr[k]
            ny += dy*arr[k]
        result = min(result,((Xb-nx)**2+(Yb-ny)**2)**0.5)
    dx,dy = M[S[i]]
    x,y = x+dx,y+dy

print(result)