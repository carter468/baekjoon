# 벽록의 가면
# Gold 4, bruteforcing, geometry

import itertools

def CCW(a,b,c): 
    return a[0]*b[1]+b[0]*c[1]+c[0]*a[1]-b[0]*a[1]-c[0]*b[1]-a[0]*c[1] > 0

def check(a,b,c,d):
    for a,b,c,d in (a,b,c,d),(a,b,d,c),(a,c,b,d):
        r1,r2,r3,r4 = CCW(a,b,c),CCW(b,c,d),CCW(c,d,a),CCW(d,a,b)
        if r1 == r2 == r3 == r4: return 1
    return 0

arr = [tuple(map(int,input().split())) for _ in range(int(input()))]

count = 0
for a,b,c,d in itertools.combinations(arr,4):
    count += check(a,b,c,d)
print(count)