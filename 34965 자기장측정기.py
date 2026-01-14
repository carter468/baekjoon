# 자기장 측정기
# Gold 5, implementation, simulation

D = (1,0),(0,1),(-1,0),(0,-1)

x0,y0 = map(int,input().split())
m = x0**2+y0**2
result = 0,0
x,y = 0,0
d = 0
q = input()
i = 0
while i < len(q):
    if q[i] == 'S':
        i += 1
        a = ''
        while i < len(q) and q[i] not in 'ST':
            a += q[i]
            i += 1
        a = int(a)
        dx,dy = D[d]
        nx = x+dx*a
        ny = y+dy*a
        if dx == 0:
            a,b = min(y,ny),max(y,ny)
            if x == x0 and a <= y0 <= b: exit(print(-1))
            if y0 < a: t = a
            elif y0 > b: t = b
            else: t = y0
            if (nx-x0)**2+(t-y0)**2 < m:
                m = (nx-x0)**2+(t-y0)**2
                result = nx,t
        else:
            a,b = min(x,nx),max(x,nx)
            if y == y0 and a <= x0 <= b: exit(print(-1))
            if x0 < a: t = a
            elif x0 > b: t = b
            else: t = x0
            if (ny-y0)**2+(t-x0)**2 < m:
                m = (ny-y0)**2+(t-x0)**2
                result = t,ny
        x,y = nx,ny
    else:
        i += 1
        a = int(q[i])
        d = (d+a)%4
        if (x,y) == (x0,y0): exit(print(-1))
        i += 1
print(*result)