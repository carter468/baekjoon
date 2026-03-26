# Area Between Outer Hull and Inner Hull
# Platinum 4, convex hull

import sys
input = sys.stdin.readline

def ccw(p1,p2,p3):
    return (p2[0]-p1[0])*(p3[1]-p1[1])-(p2[1]-p1[1])*(p3[0]-p1[0])

def convexHull(P):
    P.sort()

    lower = []
    for p in P:
        while len(lower) >= 2 and ccw(lower[-2],lower[-1],p) <= 0:
            lower.pop()
        lower.append(p)

    upper = []
    for p in reversed(P):
        while len(upper) >= 2 and ccw(upper[-2],upper[-1],p) <= 0:
            upper.pop()
        upper.append(p)

    hull = lower[:-1]+upper[:-1]
    hull_set = set(hull)
    inner = [p for p in P if p not in hull_set]

    return hull,inner

def area(hull):
    p = hull[0]
    result = 0
    for i in range(2,len(hull)):
        result += ccw(p,hull[i-1],hull[i])
    return result

while True:
    ID,N = input().split()
    N = int(N)
    if N == 0: break

    P = [tuple(map(float,input().split())) for _ in range(N)]

    hull,P = convexHull(P)
    ho = area(hull)

    hull,P = convexHull(P)
    hi = area(hull)

    print(f'ProblemID {ID}: {(ho-hi)/2:.4f}')