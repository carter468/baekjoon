# 동물원 확장
# Platinum 5, binary search

def f(x,arr):
    def g(y):
        c = 0
        for a,b in arr:
            if a <= y: c += (y-a)//b+1
        return c

    lo,hi = 0,T
    while lo+1 < hi:
        mid = (lo+hi)//2
        if g(mid) >= x: hi = mid
        else: lo = mid 
    return hi

def check(x):
    return f(x,A)+f(x,B) <= T

T = int(input())
A = [tuple(map(int,input().split())) for _ in range(int(input()))]
B = [tuple(map(int,input().split())) for _ in range(int(input()))]

lo,hi = 0,T*50
while lo+1 < hi:
    mid = (lo+hi)//2
    if check(mid): lo = mid
    else: hi = mid
print(f(lo,A))