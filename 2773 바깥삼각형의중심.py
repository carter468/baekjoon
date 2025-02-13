# 바깥 삼각형의 중심
# Gold 3, geometry

def ccw(x1,y1,x2,y2,x3,y3):
    return x1*y2+x2*y3+x3*y1-x2*y1-x3*y2-x1*y3

def find(x1,y1,x2,y2,x3,y3):
    dx,dy = x2-x1,y2-y1
    for i in (1,-1):
        x4,y4 = x1+dy*i,y1-dx*i
        x5,y5 = x2+dy*i,y2-dx*i
        if ccw(x1,y1,x2,y2,x5,y5)*ccw(x1,y1,x2,y2,x3,y3) < 0:
            return x4,y4,x5,y5

for _ in range(int(input())):
    Ax,Ay,Bx,By,Cx,Cy = *map(float,input().split()),*map(float,input().split()),*map(float,input().split())
    
    Dx,Dy,Ex,Ey = find(Ax,Ay,Bx,By,Cx,Cy)
    Jx,Jy,_,_ = find(Bx,By,Cx,Cy,Ax,Ay)
    _,_,Gx,Gy = find(Cx,Cy,Ax,Ay,Bx,By)
    Lx,Ly = (Dx+Gx)/2,(Dy+Gy)/2
    Mx,My = (Ex+Jx)/2,(Ey+Jy)/2

    a1,b1,c1 = Ay-Ly,Lx-Ax,Ax*Ly-Lx*Ay
    a2,b2,c2 = By-My,Mx-Bx,Bx*My-Mx*By
    d = a1*b2-a2*b1
    x,y = (c2*b1-c1*b2)/d,(a2*c1-a1*c2)/d

    print(f'{x+0.00001:.4f} {y+0.00001:.4f}')