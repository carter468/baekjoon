# 구간 합 구하기 2
# Platinum 4, lazy propagation

import sys
input = sys.stdin.readline

def init(x,s,e):
    if s == e:
        seg[x] = arr[s]
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

n,m,k = map(int,input().split())
arr = [int(input()) for _ in range(n)]

seg = [0]*(n*4)
lazy = [0]*(n*4)
init(1,0,n-1)

for _ in range(m+k):
    q = tuple(map(int,input().split()))
    if q[0] == 1:
        update(1,0,n-1,q[1]-1,q[2]-1,q[3])
    else:
        print(query(1,0,n-1,q[1]-1,q[2]-1))