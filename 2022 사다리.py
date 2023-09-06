# 사다리
# Gold 4, geometry, binary search

x,y,c = map(float,input().split())

l,r = 0,min(x,y)
x,y = x*x,y*y
while 1:
    mid = (l+r)/2
    h1 = (x-mid**2)**0.5
    h2 = (y-mid**2)**0.5
    h3 = h1*h2/(h1+h2)
    if abs(c-h3) <= 1e-3:
        print(mid)
        break
    if c < h3: l = mid
    else: r = mid