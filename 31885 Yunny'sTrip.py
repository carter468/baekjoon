# Yunny's Trip
# Gold 3, ad hoc

import sys
input = sys.stdin.readline

n,k = map(int,input().split())
arr = set([tuple(map(int,input().split())) for _ in range(n)])
ex,ey = map(int,input().split())

result = abs(ex)+abs(ey)
for x,y in arr:
    result = min(result,2+abs(ex-x)+abs(ey-y))
    for nx,ny in (x+1,y),(x-1,y),(x,y+1),(x,y-1):
        if (nx,ny) == (ex,ey): result = min(result,3)
    if (ex-x,ey-y) in arr: result = min(result,4)
    for nx,ny in (ex+1,ey),(ex-1,ey),(ex,ey+1),(ex,ey-1):
        if (nx-x,ny-y) in arr: result = min(result,5)
print(result if result <= k else -1)
