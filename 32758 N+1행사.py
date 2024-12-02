# N+1 행사
# Gold 4, binary search

def check(k):
    count = k
    while True:
        p,k = divmod(k,x)
        if p == 0: return count >= y
        count += p
        k += p

M = int(input())
n = tuple(map(int,input().split()))
a = tuple(map(int,input().split()))

for i in range(M):
    x,y = n[i],a[i]
    if x == 1:
        print(min(1,y),end=' ')
        continue
    lo,hi = -1,10**9
    while lo+1 < hi:
        mid = (lo+hi)//2
        if check(mid): hi = mid
        else: lo = mid
    print(hi,end=' ')