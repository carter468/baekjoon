# 땅 자르기
# Gold 4, geometry, case work

def area(p1,p2,p3):
    x1,y1,x2,y2,x3,y3 = *p1,*p2,*p3
    return abs(x1*y2+x2*y3+x3*y1-x1*y3-x2*y1-x3*y2)/2

def check(p1,p2,p3):
    global result
    x = area(p1,p2,p3)*2
    if abs(t-x) < result[0]: result = [abs(t-x),x]

def mid(p1,p2):
    x1,y1,x2,y2 = *p1,*p2
    return (x1+x2)/2,(y1+y2)/2

a,b,c,d,e,f,g,h = map(int,input().split())
p = (a,b),(c,d),(e,f),(g,h)

t = area(p[0],p[1],p[2])+area(p[0],p[2],p[3])
result = [t,0]

for i in range(4):
    p1,p2 = p[i],p[i-1]

    for p3 in (p[i-2],p[i-3]):
        check(p1,p2,p3)

    for j in range(3):
        p3,p4 = p[i-1-j],p[i-2-j]
        check(p1,p2,mid(p3,p4))

m1,m2 = mid(p[-1],p[-2]),mid(p[-3],p[0])
x = (area(p[0],p[-1],m1)+area(p[0],m1,m2))*2
if abs(t-x) < result[0]: result = [abs(t-x),x]

m1,m2 = mid(p[0],p[-1]),mid(p[-2],p[-3])
x = (area(p[0],m1,m2)+area(p[0],m2,p[-3]))*2
if abs(t-x) < result[0]: result = [abs(t-x),x]

x = result[1]/2
print(*sorted((x,t-x)))