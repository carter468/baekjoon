# 평행사변형

def dist(a,b,c,d):
    return ((a-c)**2+(b-d)**2)**0.5

def check(a,b,c,d,e,f):
    if a==c and c==e:
        return True
    if (a==c and c!=e) or (a!=c and c==e):
        return False
    if (d-b)/(c-a) == (f-d)/(e-c):
        return True
    return False

x1,y1,x2,y2,x3,y3 = map(int,input().split())
if check(x1,y1,x2,y2,x3,y3):
    print(-1)
else:
    d1 = dist(x1,y1,x2,y2)
    d2 = dist(x2,y2,x3,y3)
    d3 = dist(x1,y1,x3,y3)
    d = [d1,d2,d3]
    d.sort()
    print((d[2]-d[0])*2)