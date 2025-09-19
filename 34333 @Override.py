# @Override
# Platinum 3, ETT, lazy prop

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(x,p,m):
    global idx
    idx += 1
    l[x] = idx
    B[idx] = A[x-1]
    v[idx] = m
    m = max(m,A[x-1])
    for nx in graph[x]:
        if nx != p:
            dfs(nx,x,m)
    r[x] = idx

def init(x,s,e):
    if s == e:
        seg[x] = B[s]
        return seg[x]
    m = (s+e)//2
    seg[x] = init(x*2,s,m)+init(x*2+1,m+1,e)
    return seg[x]

def init1(x,s,e):
    if s == e:
        seg1[x] = v[s]
        return seg1[x]
    m = (s+e)//2
    seg1[x] = max(init1(x*2,s,m),init1(x*2+1,m+1,e))
    return seg1[x]

def propagation(x,s,e):
    if lazy[x]:
        seg[x] = (e-s+1)*lazy[x]
        if s != e:
            lazy[x*2] = lazy[x]
            lazy[x*2+1] = lazy[x]
        lazy[x] = 0

def propagation1(x,s,e):
    if lazy1[x]:
        seg1[x] = lazy1[x]
        if s != e:
            lazy1[x*2] = lazy1[x]
            lazy1[x*2+1] = lazy1[x]
        lazy1[x] = 0

def update(x,l,r,s,e,dif):
    propagation(x,l,r)

    if r < s or e < l: return
    if s <= l and r <= e:
        seg[x] = (r-l+1)*dif
        if l != r:
            lazy[x*2] = dif
            lazy[x*2+1] = dif
        return
    
    m = (l+r)//2
    update(x*2,l,m,s,e,dif)
    update(x*2+1,m+1,r,s,e,dif)
    seg[x] = seg[x*2]+seg[x*2+1]

def update1(x,l,r,s,e,dif):
    propagation1(x,l,r)

    if r < s or e < l: return
    if s <= l and r <= e:
        seg1[x] = dif
        if l != r:
            lazy1[x*2] = dif
            lazy1[x*2+1] = dif
        return
    
    m = (l+r)//2
    update1(x*2,l,m,s,e,dif)
    update1(x*2+1,m+1,r,s,e,dif)
    seg1[x] = max(seg1[x*2],seg1[x*2+1]) 

def query(x,l,r,s,e):
    propagation(x,l,r)

    if r < s or e < l: return 0
    if s <= l and r <= e: return seg[x]
    m = (l+r)//2
    return query(x*2,l,m,s,e)+query(x*2+1,m+1,r,s,e)

def query1(x,l,r,s,e):
    propagation1(x,l,r)

    if r < s or e < l: return -10**9
    if s <= l and r <= e: return seg1[x]
    m = (l+r)//2
    return max(query1(x*2,l,m,s,e),query1(x*2+1,m+1,r,s,e))

N,Q = map(int,input().split())
A = tuple(map(int,input().split()))
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

l = [0]*(N+1)
r = [0]*(N+1)
v = [0]*N
idx = -1
B = [0]*N
dfs(1,1,A[0])

seg = [0]*(N*4)
lazy = [0]*(N*4)
init(1,0,N-1)

seg1 = [-10**9]*(N*4)
lazy1 = [0]*(N*4)
init1(1,0,N-1)

for _ in range(Q):
    q,i = map(int,input().split())
    if q == 1:
        x = query1(1,0,N-1,l[i],l[i])
        update(1,0,N-1,l[i],r[i],x)
        update1(1,0,N-1,l[i],r[i],x)
    else:
        print(query(1,0,N-1,l[i],r[i]))