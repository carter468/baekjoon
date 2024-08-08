# SoleMap
# Gold 4, prefix sum, math

def solve(c,w):
    x,y = divmod(c,w)
    print(x*x*(w-y)+(x+1)*(x+1)*y)

n,m = map(int,input().split())
w = tuple(map(int,input().split()))

arr = [0]*n
for _ in range(m):
    u,v,x = map(int,input().split())
    arr[u-1] += x
    arr[v-1] -= x

for i in range(n-1):
    arr[i+1] += arr[i]
    solve(arr[i],w[i])
