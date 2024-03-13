# 물통
# Gold 5, DFS

def move(x,y,z,m):
    w = x+y
    if w > m: return w-m,m,z
    else: return 0,w,z

def check(nx,ny,nz):
    if (nx,ny,nz) not in visited:
        visited.add((nx,ny,nz))
        q.append((nx,ny,nz))

a,b,c = map(int,input().split())

result = set()
visited = set([(0,0,c)])
q = [(0,0,c)]
while q:
    x,y,z = q.pop()
    if x == 0: result.add(z)
    nx,ny,nz = move(x,y,z,b)
    check(nx,ny,nz)
    ny,nx,nz = move(y,x,z,a)
    check(nx,ny,nz)
    nx,nz,ny = move(x,z,y,c)
    check(nx,ny,nz)
    nz,nx,ny = move(z,x,y,a)
    check(nx,ny,nz)
    ny,nz,nx = move(y,z,x,c)
    check(nx,ny,nz)
    nz,ny,nx = move(z,y,x,b)
    check(nx,ny,nz)
print(*sorted(result))