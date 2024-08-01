# Square, Not Rectangle
# Gold 4, binary search

def check(x):
    count = 0
    for a in arr:
        if a >= x:
            count += 1
            if count == x: return True
        else: count = 0
    return False

input()
arr = tuple(map(int,input().split()))

lo,hi = 1,10**9+1
while lo+1 < hi:
    mid = (lo+hi)//2
    if check(mid): lo = mid
    else: hi = mid
print(lo)