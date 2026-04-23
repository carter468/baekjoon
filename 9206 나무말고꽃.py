# 나무 말고 꽃
# Platinum 3, calculus

import math
DIV = 0.00005

def f(x,a,b):
    return a*math.exp(-(x*x))+b*math.sqrt(x)

def g(x,a,b):
    return math.pi*f(x,a,b)**2

def get_volume(a,b,h):
    n = int(math.ceil(h/DIV))
    interval = h/n

    volume = 0
    for i in range(n):
        xa = interval*i
        xb = interval*(i+1)
        xm = (xa+xb)/2

        volume += (interval/6)*(g(xa,a,b)+4*g(xm,a,b)+g(xb,a,b))

    return volume

V,N = input().split()
V = float(V)
N = int(N)

min_gap = float("inf")

for i in range(N):
    a,b,h = map(float,input().split())

    gap = abs(get_volume(a,b,h)-V)
    if gap < min_gap:
        min_gap = gap
        result = i

print(result)