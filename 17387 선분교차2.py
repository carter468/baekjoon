# 선분교차2

x1,y1,x2,y2 = map(int,input().split())
x3,y3,x4,y4 = map(int,input().split())

def ccw(x1,y1,x2,y2,x3,y3):
    return x1*y2 + x2*y3 + x3*y1 - (x2*y1 + x3*y2 + x1*y3)
    
abc = ccw(x1,y1,x2,y2,x3,y3)
abd = ccw(x1,y1,x2,y2,x4,y4)
cda = ccw(x3,y3,x4,y4,x1,y1)
cdb = ccw(x3,y3,x4,y4,x2,y2)
mx1, my1, mx2, my2 = min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2)
mx3, my3, mx4, my4 = min(x3, x4), min(y3, y4), max(x3, x4), max(y3, y4)
ans = 0
if abc*abd == 0 and cda*cdb == 0:
    if mx1 <= mx4 and mx3 <= mx2 and my1 <= my4 and my3 <= my2:
        ans = 1
elif abc*abd <= 0 and cda*cdb <= 0:
    ans = 1
print(ans)