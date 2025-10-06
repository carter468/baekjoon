# 전봇대
# Platinum 5, ternary search

def f(x):
    r = 0
    for i in range(N):
        r += abs(x*i-X[i])
    return r

N = int(input())
X = tuple(map(int,input().split()))

lo,hi = 0,X[-1]
while hi-lo > 3:
    m1 = (lo*2+hi)//3
    m2 = (lo+hi*2)//3
    if f(m1) < f(m2): hi = m2
    else: lo = m1

print(min([f(i) for i in range(lo,hi+1)]))