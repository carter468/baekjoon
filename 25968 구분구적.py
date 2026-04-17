# 구분구적
# Gold 2, math, binary search

f = lambda x: sum(A[i]*x**(N*2-i*2) for i in range(N+1))

N = int(input())
A = tuple(map(float,input().split()))
K = int(input())//2

t = 1 if f(0) > 0 else -1
lo,hi = 0,32
for _ in range(55):
    mid = (lo+hi)/2
    if f(mid)*t > 0: lo = mid
    else: hi = mid

v = hi/K
e = v/2
print(sum([f(e+v*i) for i in range(K)])*t*v*2)