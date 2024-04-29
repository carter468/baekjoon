# 급상승
# Gold 5, binary search

n,k = map(int,input().split())
arr = tuple(map(int,input().split()))

lo,hi = 0,10**18
while lo+1 < hi:
    mid = (lo+hi)//2
    x = 0
    for i in range(n-1):
        a = min(arr[i+1]-arr[i],mid)
        x += (mid*2-a+1)*a//2
    x += mid*(mid+1)//2
    if x >= k: hi = mid
    else: lo = mid
print(hi)