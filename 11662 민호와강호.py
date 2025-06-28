# 민호와 강호
# Gold 4, geometry, ternary search

def f(k):
    def g(x1,y1,x2,y2,k):
        return x2*k+x1*(1-k),y2*k+y1*(1-k)
    
    def dist(x1,y1,x2,y2):
        return ((x1-x2)**2+(y1-y2)**2)**0.5

    return dist(*g(Ax,Ay,Bx,By,k),*g(Cx,Cy,Dx,Dy,k))
    
Ax,Ay,Bx,By,Cx,Cy,Dx,Dy = map(int,input().split())

lo,hi = 0,1
while hi-lo >= 1e-9:
    m1,m2 = (lo*2+hi)/3,(lo+hi*2)/3
    d1,d2 = f(m1),f(m2)
    if d1 > d2: lo = m1
    else: hi = m2
print(f(hi))