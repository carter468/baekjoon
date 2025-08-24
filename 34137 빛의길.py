# 빛의 길
# Platinum 3, lazy prop, sweeping

import sys
input = sys.stdin.readline

def propagation(node,start,end):
    if lazy[node] != 0:
        tree[node] = lazy[node]*(end-start+1)
        if start != end:
            lazy[node*2] = lazy[node]
            lazy[node*2+1] = lazy[node]
        lazy[node] = 0

def update(node,start,end,l,r,height):
    propagation(node,start,end)
    if r < start or end < l:
        return
    if l <= start and end <= r:
        lazy[node] = height
        propagation(node,start,end)
        return
    
    mid = (start+end)//2
    update(node*2,start,mid,l,r,height)
    update(node*2+1,mid+1,end,l,r,height)
    tree[node] = tree[node*2]+tree[node*2+1]

def query(node,start,end,l,r):
    propagation(node,start,end)
    if r < start or end < l:
        return 0
    if l <= start and end <= r:
        return tree[node]

    mid = (start+end)//2
    return query(node*2,start,mid,l,r)+query(node*2+1,mid+1,end,l,r)

def final(node,start,end):
    propagation(node,start,end)
    if start == end:
        result[A[end]-1] += N-tree[node]
        return
    
    mid = (start+end)//2
    final(node*2,start,mid)
    final(node*2+1,mid+1,end)

N,M,T,K = map(int,input().split())
A = tuple(map(int,input().split()))

tree = [0]*(M*4)
lazy = [0]*(M*4)

result = [0]*T
for r,s,e,c in sorted([tuple(map(int,input().split())) for _ in range(K)],reverse=True):
    s,e = s-1,e-1
    result[c-1] += (N-r+1)*(e-s+1)-query(1,0,M-1,s,e)
    update(1,0,M-1,s,e,N-r+1)
final(1,0,M-1)

print(*result)