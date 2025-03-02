# 콘센트
# Gold 4, binary search, greedy

def check(x):
    t = [x]*M
    for a in arr:
        if t[-1] >= a:
            t.append(t.pop()-a)
            t.sort()
        else: return False
    return True

N,M = map(int,input().split())
arr = sorted(map(int,input().split()),reverse=True)

lo,hi = 0,10**9
while lo+1 < hi:
    mid = (lo+hi)//2
    if check(mid): hi = mid
    else: lo = mid
print(hi)