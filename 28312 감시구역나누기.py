# 감시 구역 나누기
# Gold 2, binary search

def check(m):
    count,s,c,t = 0,0,0,0
    for i,x in enumerate(arr):
        c += 1
        s += c*x
        t += s
        if t > m:
            s,c,t = 0,0,0
            count += 1
            if i == N-2: count += 1
    if t: count += 1
    return count <= M

for _ in range(int(input())):
    N,M = map(int,input().split())
    arr = tuple(map(int,input().split()))

    lo,hi = -1,10**20
    while lo+1 < hi:
        mid = (lo+hi)//2
        if check(mid): hi = mid
        else: lo = mid
    print(hi)