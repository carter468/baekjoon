# 전기 요금
# Gold 4, implementation, binary search

P1 = 200
P2 = P1+(10000-100)*3
P3 = P2+(1000000-10000)*5

def f(x):
    if x <= 100: return x*2
    elif x <= 10000: return P1+(x-100)*3
    elif x <= 1000000: return P2+(x-10000)*5
    else: return P3+(x-1000000)*7

while True:
    A,B = map(int,input().split())
    if A == 0: break

    if A <= P1: x = A//2
    elif A <= P2: x = (A-P1)//3+100
    elif A <= P3: x = (A-P2)//5+10000
    else: x = (A-P3)//7+1000000

    lo,hi = 0,x//2+1
    while True:
        mid = (lo+hi)//2
        k = f(x-mid)-f(mid)
        if k == B: 
            print(f(mid))
            break
        if k > B: lo = mid
        else: hi = mid