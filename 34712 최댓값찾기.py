# 최댓값 찾기
# Gold 2, binary search

import sys

N = int(input())

print('? 100000')
sys.stdout.flush()
m = int(input())

lo,hi = 0,100000
while lo+1 < hi:
    mid = (lo+hi)//2
    print('?',mid)
    sys.stdout.flush()
    x = int(input())
    if m-x == (100000-mid)*N: hi = mid
    else: lo = mid
print('!',hi)