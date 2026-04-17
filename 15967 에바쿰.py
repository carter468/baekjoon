# 에바쿰
# Platinum 4, lazy prop

import sys
input = sys.stdin.readline

def init(x,s,e):
    if s == e:
        seg[x] = A[s]
        return seg[x]
    m = (s+e)//2
    seg[x] = init(x*2,s,m)+init(x*2+1,m+1,e)
    return seg[x]

def propagation(x,s,e):
    if lazy[x]:
        seg[x] += (e-s+1)*lazy[x]
        if s != e:
            lazy[x*2] += lazy[x]
            lazy[x*2+1] += lazy[x]
        lazy[x] = 0

def update(x,l,r,s,e,dif):
    propagation(x,l,r)

    if r < s or e < l: return
    if s <= l and r <= e:
        seg[x] += (r-l+1)*dif
        if l != r:
            lazy[x*2] += dif
            lazy[x*2+1] += dif
        return
    
    m = (l+r)//2
    update(x*2,l,m,s,e,dif)
    update(x*2+1,m+1,r,s,e,dif)
    seg[x] = seg[x*2]+seg[x*2+1]

def query(x,l,r,s,e):
    propagation(x,l,r)

    if r < s or e < l: return 0
    if s <= l and r <= e: return seg[x]
    m = (l+r)//2
    return query(x*2,l,m,s,e)+query(x*2+1,m+1,r,s,e)

N,Q1,Q2 = map(int,input().split())
A = tuple(map(int,input().split()))

seg = [0]*(N*4)
lazy = [0]*(N*4)
init(1,0,N-1)

result = []
for _ in range(Q1+Q2):
    q = tuple(map(int,input().split()))
    if q[0] == 1:
        n,m = q[1:]
        result.append(query(1,0,N-1,n-1,m-1))
    else:
        s,e,l = q[1:]
        update(1,0,N-1,s-1,e-1,l)
print(*result,sep='\n')