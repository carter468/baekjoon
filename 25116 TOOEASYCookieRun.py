# TOO EASY Cookie Run
# Gold 4, binary search, two pointer

def check(x):
    count = 0
    l,r = 0,0
    t = A[0]+x
    while r < N:
        if t >= M:
            count += N-r
            t -= A[l]+x
            l += 1
        else:
            r += 1
            if r < N: t += A[r]+x
    return count >= K

N,M,K = map(int,input().split())
A = tuple(map(int,input().split()))

lo,hi = -1,M
while lo+1 < hi:
    mid = (lo+hi)//2
    if check(mid): hi = mid
    else: lo = mid
print(hi)