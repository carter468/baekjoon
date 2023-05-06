# 두 원
# Gold 2, 기하학

import math

x1,y1,r1,x2,y2,r2 = map(float,input().split())

d = ((x1-x2)**2+(y1-y2)**2)**.5
if r1+r2<=d:
    answer = 0
elif r1>=r2 and d<=r1-r2:
    answer = r2**2*math.pi
elif r2>=r1 and d<=r2-r1:
    answer = r1**2*math.pi
else:
    a1 = math.acos((r1**2+d**2-r2**2)/(2*r1*d))*2
    a2 = math.acos((r2**2+d**2-r1**2)/(2*r2*d))*2
    answer = (r1**2*(a1-math.sin(a1))+r2**2*(a2-math.sin(a2)))/2

print("%.3f"%answer)