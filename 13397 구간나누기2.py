# 구간 나누기 2
# Gold 4, parametric search

def check(x):
    count = 1
    a,b = 10000,1
    for c in arr:
        a,b = min(a,c),max(b,c)
        if b-a > x:
            count += 1
            a,b = c,c
    return count <= m

n,m = map(int,input().split())
arr = tuple(map(int,input().split()))

lo,hi = -1,9999
while lo+1 < hi:
    mid = (lo+hi)//2
    if check(mid): hi = mid
    else: lo = mid
print(hi)
