# 사과나무
# Gold 4, geometry

def CCW(a1,b1,a2,b2,a3,b3):
    return abs(a1*b2+a2*b3+a3*b1-a2*b1-a3*b2-a1*b3)

x1,y1 = map(int,input().split())
x2,y2 = map(int,input().split())
x3,y3 = map(int,input().split())
s = CCW(x1,y1,x2,y2,x3,y3)

count = 0
for _ in range(int(input())):
    p1,p2 = map(int,input().split())
    if CCW(x1,y1,p1,p2,x2,y2)+CCW(x2,y2,p1,p2,x3,y3)+CCW(x3,y3,p1,p2,x1,y1) == s: count += 1
print(s/2)
print(count)