# 효율적인 애니메이션 감상
# Gold 3, greedy, binary search

def check(x):
    t = 0
    while x >= 0:
        t += L[x]
        x -= K
    return t <= M

N,M,K = map(int,input().split())
L = sorted(map(int,input().split()))

lo,hi = -1,N
while lo+1 < hi:
    mid = (lo+hi)//2
    if check(mid): lo = mid
    else: hi = mid
print(lo+1)