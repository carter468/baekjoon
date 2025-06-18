# Circle Through Three Points
# Gold 4, math, geometry

def get_line(a,b,c,d):
    return (c-a)/(b-d),(a-c)*(a+c)/2/(b-d)+(b+d)/2

def get_point(a,b,c,d):
    x = (d-b)/(a-c)
    y = a*x+b
    return x,y

while True:
    try: Ax,Ay,Bx,By,Cx,Cy = map(float,input().split())
    except: break

    l1 = get_line(Ax,Ay,Bx,By)
    l2 = get_line(Bx,By,Cx,Cy)

    rx,ry = get_point(*l1,*l2)
    r = ((Ax-rx)**2+(Ay-ry)**2)**0.5
    
    if rx >= 0: sx = f'(x - {rx:.3f})^2'
    else: sx = f'(x + {-rx:.3f})^2'

    if ry >= 0: sy = f'(y - {ry:.3f})^2'
    else: sy = f'(y + {-ry:.3f})^2'

    print(f'{sx} + {sy} = {r:.3f}^2')

    c = -rx*2
    if c >= 0: sx = f'+ {c:.3f}x'
    else: sx = f'- {-c:.3f}x'
    d = -ry*2
    if d >= 0: sy = f'+ {d:.3f}y'
    else: sy = f'- {-d:.3f}y'
    e = rx**2+ry**2-r**2
    if e >= 0: sr = f'+ {e:.3f}'
    else: sr = f'- {-e:.3f}'
    print(f'x^2 + y^2 {sx} {sy} {sr} = 0')
    print()