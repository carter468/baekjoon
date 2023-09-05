# 선분과 점
# Gold 5, geometry, ternary search

def dist(x,y,z):
    return ((x-cx)**2+(y-cy)**2+(z-cz)**2)**0.5

ax,ay,az,bx,by,bz,cx,cy,cz = map(int,input().split())

result = float('inf')
while 1:
    mx,my,mz = (ax+bx)/2,(ay+by)/2,(az+bz)/2
    l = dist(ax,ay,az)
    h = dist(mx,my,mz)
    r = dist(bx,by,bz)

    if abs(result-h) <= 1e-6: break
    result = min(result,h)
    if l > r: ax,ay,az = mx,my,mz
    else: bx,by,bz = mx,my,mz
print(result)