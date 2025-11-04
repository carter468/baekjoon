# Steps
# Gold 5, binary search

def check(x):
    if x%2 == 0:
        t = x//2
        return t*(t+1) >= a
    else:
        t = x//2+1
        return t*t >= a

for _ in range(int(input())):
    x,y = map(int,input().split())
    a = y-x
    lo,hi = -1,92681
    while lo+1 < hi:
        mid = (lo+hi)//2
        if check(mid): hi = mid
        else: lo = mid
    print(hi)