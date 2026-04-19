# 폭탄의 악마
# Gold 3, binary search

def check(r):
    b = 0
    i = 0
    m = INF
    while i < N:
        x,c = XC[i]
        m = min(m,c)
        if i+1 < N and x+r < XC[i+1][0]:
            b += m
            m = INF
        i += 1
    b += m
    return b <= B

INF = 10**9

N = int(input())
XC = sorted(zip(map(int,input().split()),map(int,input().split())))
B = int(input())

lo,hi = 0,INF
while lo+1 < hi:
    mid = (lo+hi)//2
    if check(mid): hi = mid
    else: lo = mid
print(hi)