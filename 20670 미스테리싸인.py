# 미스테리 싸인
# Platinum 3, point in convex polygon, binary search

def in_polygon(hull,x,y):
    def CCW(x1,y1,x2,y2,x3,y3):
        return x1*y2+x2*y3+x3*y1-x2*y1-x3*y2-x1*y3
    
    n = len(hull)//2
    lo,hi = 0,n
    while lo+1 < hi:
        mid = (lo+hi)//2
        if CCW(hull[0],hull[1],x,y,hull[mid*2],hull[mid*2+1]) < 0: lo = mid
        else: hi = mid
    hi %= n
    return CCW(x,y,hull[lo*2],hull[lo*2+1],hull[hi*2],hull[hi*2+1]) > 0

N,M,K = map(int,input().split())
A = tuple(map(int,input().split()))
B = tuple(map(int,input().split()))
P = tuple(map(int,input().split()))

count = 0
for i in range(K):
    x,y = P[i*2],P[i*2+1]
    if not in_polygon(A,x,y) or in_polygon(B,x,y):
        count += 1

print(count if count else 'YES')