# 킥보드로 등교하기
# Gold 4, binary search

l,n,k = map(int,input().split())
arr = list(map(int,input().split()))+[l]

lo,hi = 0,200000
while lo+1 < hi:
    mid = (lo+hi)//2
    x = mid
    count = 0
    i = 0
    for a in arr:
        if a-i > mid:
            count = k+1
            break
        x -= a-i
        if x < 0:
            x = mid-(a-i)
            count += 1
        i = a
    if count <= k: hi = mid
    else: lo = mid
print(hi)