# 시간을 돌리고 싶어
# Gold 5, binary search

import bisect

def check(x):
    i = n-1
    for _ in range(k):
        if i-x <= 0: return True
        i = arr[bisect.bisect_left(arr,i-x)]
    return False

n,k = map(int,input().split())
arr = []
for i,a in enumerate(input().split()):
    if a == '1': arr.append(i)

lo,hi = 0,n
while lo+1 < hi:
    mid = (lo+hi)//2
    if check(mid): hi = mid
    else: lo = mid
print(hi)
