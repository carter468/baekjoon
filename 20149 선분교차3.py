# 선분교차3

x1,y1,x2,y2 = map(int,input().split())
x3,y3,x4,y4 = map(int,input().split())

def ccw(x1,y1,x2,y2,x3,y3):
    return x1*y2 + x2*y3 + x3*y1 - (x2*y1 + x3*y2 + x1*y3)

def intersection(x1,y1,x2,y2,x3,y3,x4,y4):
    if x1==x2 and x3==x4:
        if y1==y3 or y1==y4:
            return x1,y1
        elif y2==y3 or y2==y4:
            return x2,y2
    if x1==x2:
        c = (y4-y3)/(x4-x3)
        d = y3-(y4-y3)/(x4-x3)*x3
        return x1, c*x1 + d
    if x3==x4:
        a = (y2-y1)/(x2-x1) 
        b = y1-(y2-y1)/(x2-x1)*x1
        return x3,a*x3+b

    a = (y2-y1)/(x2-x1) 
    b = y1-(y2-y1)/(x2-x1)*x1
    c = (y4-y3)/(x4-x3)
    d = y3-(y4-y3)/(x4-x3)*x3

    if a==c:
        if y1==y3 or y1==y4:
            return x1,y1
        elif y2==y3 or y2==y4:
            return x2,y2
    return (b-d)/(c-a),(b*c-a*d)/(c-a)
    
abc = ccw(x1,y1,x2,y2,x3,y3)
abd = ccw(x1,y1,x2,y2,x4,y4)
cda = ccw(x3,y3,x4,y4,x1,y1)
cdb = ccw(x3,y3,x4,y4,x2,y2)
mx1, my1, mx2, my2 = min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2)
mx3, my3, mx4, my4 = min(x3, x4), min(y3, y4), max(x3, x4), max(y3, y4)

if mx1>mx4 or mx3>mx2 or my1>my4 or my3>my2:
    print(0)
elif abc*abd <= 0 and cda*cdb <= 0:
    print(1)
    if (x4-x3)*(y2-y1) == (x2-x1)*(y4-y3):
        if mx2 == mx3 or mx4 == mx1:
            if [x1,y1] == [x3,y3] or [x1,y1] == [x4,y4]:
                print(x1,y1)
            elif [x2,y2] == [x3,y3] or [x2,y2] == [x4,y4]:
                print(x2,y2)
    else:
        print(*intersection(x1,y1,x2,y2,x3,y3,x4,y4))
else:
    print(0)

# if abc*abd == 0 and cda*cdb == 0:   # 세 점이 한직선위에 있다.
#     if mx2 == mx3 and my2 == my3:   
#         print(1)
#         print(mx2,my2)
#     elif mx1 < mx4 and mx3 < mx2 and my1 < my4 and my3 < my2:
#         print(1)
#     elif (x1,y1) == (x3,y3) or (x1,y1) == (x4,y4):
#         print(1)
#         print(x1,y1)
#     elif (x2,y2) == (x3,y3) or (x2,y2) == (x4,y4):
#         print(1)
#         print(x2,y2)
#     else:
#         print(0)
# elif abc*abd <= 0 and cda*cdb <= 0:     # 교차한다.
#     print(1)
#     x,y = intersection(x1,y1,x2,y2,x3,y3,x4,y4)
#     print(x,y)

# else:
#     print(0)