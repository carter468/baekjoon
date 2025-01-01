# 겨울이 좋아
# Gold 4, binary search

def check(x):
    c = 0
    for a in d:
        c += max(0,a-x)
    return c <= x

N = int(input())
A = tuple(map(int,input().split()))
B = tuple(map(int,input().split()))

d = []
for i in range(N):
    d.append((A[i]-1)//B[i]+1)

lo,hi = 0,10**9
while lo+1 < hi:
    mid = (lo+hi)//2
    if check(mid): hi = mid
    else: lo = mid
print(hi)