# Reconnaissance
# Gold 1, ternary search

def dist(t):
    minx,maxx = 10**9,-10**9
    for x,v in arr:
        nx = x+v*t
        minx = min(minx,nx)
        maxx = max(maxx,nx)
    return maxx-minx

while True:
    N = int(input())
    if N == 0: break

    arr = [tuple(map(int,input().split())) for _ in range(N)]
    s = set()
    for x,v in arr:
        s.add(v)
    if len(s) == 1:
        print(f'{dist(0):.2f}')
        continue

    lo,hi = 0,10**9
    while hi-lo > 1e-9:
        m1,m2 = (lo*2+hi)/3,(lo+hi*2)/3
        if dist(m1) < dist(m2):
            hi = m2
        else:
            lo = m1
    print(f'{dist(lo):.2f}')