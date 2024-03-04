# 장난을 잘 치는 토카 양
# Gold 5, binary search

def solve():
    a,b = map(int,input().split())
    c,d = map(int,input().split())
    k = int(input())

    if k == 0:
        x = (a-1)//b+1
        if x*d >= a+c: return -1
        else: return x

    x = (b-1)//k+1
    y = x*(b*2+(x-1)*-k)//2
    if y < a: return -1
    lo,hi = 0,x
    while lo+1 < hi:
        mid = (lo+hi)//2
        y = mid*(b*2+(mid-1)*-k)//2
        if y < a: lo = mid
        else: hi = mid
    if d*hi >= a+c: return -1
    else: return hi

print(solve())