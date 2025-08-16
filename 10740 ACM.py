# ACM
# Gold 1, prefix sum, DP

N = int(input())
arr = [list(map(int,input().split())) for _ in range(3)]

psum = [arr[i][:] for i in range(3)]
for i in range(3):
    for j in range(N-1,0,-1):
        psum[i][j-1] += psum[i][j]

result = 10**9
for a,b,c in (0,1,2),(0,2,1),(1,0,2),(1,2,0),(2,0,1),(2,1,0):
    x,y = 10**9,arr[a][0]
    for i in range(1,N-1):
        x = min(x,y)+arr[b][i]
        y += arr[a][i]
        result = min(result,x+psum[c][i+1])
print(result)