# 소신발언
# Gold 1, binary search, ternary search

# binary search
def check(x):
    l,r = 0,N-1
    for i in range(N):
        a,b = -(x//arr[i])+i,x//arr[i]+i
        if b < l or r < a: return False
        l,r = max(l,a),min(r,b)
    return True

N = int(input())
arr = tuple(map(int,input().split()))

lo,hi = 0,10**12
while lo+1 < hi:
    mid = (lo+hi)//2
    if check(mid): hi = mid
    else: lo = mid
print(hi)

# ternary search
def f(x):
    result = 0
    for i in range(N):
        result = max(result,abs(x-i)*arr[i])
    return result

N = int(input())
arr = tuple(map(int,input().split()))

lo,hi = 0,N-1
while lo+3 < hi:
    m1 = (lo*2+hi)//3
    m2 = (lo+hi*2)//3
    if f(m1) <= f(m2): hi = m2
    else: lo = m1

result = 10**12
for i in range(lo,hi+1):
    result = min(result,f(i))
print(result)