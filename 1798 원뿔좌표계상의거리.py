# 원뿔좌표계상의 거리
# Gold 1, math, geometry

import math

while True:
    try:
        r,h,d1,a1,d2,a2 = map(float,input().split())
    except:
        break

    a = abs(a1-a2)
    t = min(a,360-a)*r/(r*r+h*h)**0.5
    print(f'{(d1**2+d2**2-2*d1*d2*math.cos(math.radians(t)))**0.5:.2f}')