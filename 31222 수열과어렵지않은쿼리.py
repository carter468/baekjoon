# 수열과 어렵지 않은 쿼리
# Platinum 5, segtree

import sys
input = sys.stdin.readline

def merge(l1,r1,c1,l2,r2,c2):
    c = c1+c2
    if r1 == l2 and r1 != 0:
        c -= 1
    return (l1,r2,c)

def init(start,end,node):
    if start == end:
        a = A[end]
        tree[node] = (a,a,1)
        return tree[node]
    mid = (start+end)//2
    l1,r1,c1 = init(start,mid,node*2)
    l2,r2,c2 = init(mid+1,end,node*2+1)
    
    tree[node] = merge(l1,r1,c1,l2,r2,c2)
    return tree[node]

def query(start,end,node,left,right):
    if left > end or right < start:
        return (0,0,0)
    if left <= start and end <= right:
        return tree[node]
    mid = (start+end)//2
    l1,r1,c1 = query(start,mid,node*2,left,right)
    l2,r2,c2 = query(mid+1,end,node*2+1,left,right)
    
    return merge(l1,r1,c1,l2,r2,c2)

def update(start,end,node,idx):
    if idx < start or idx > end:
        return tree[node]
    if start == end:
        a = A[end]
        tree[node] = (a,a,1)
        return tree[node]
    mid = (start+end)//2
    l1,r1,c1 = update(start,mid,node*2,idx)
    l2,r2,c2 = update(mid+1,end,node*2+1,idx)
    
    tree[node] = merge(l1,r1,c1,l2,r2,c2)
    return tree[node]

N,Q = map(int,input().split())
A = list(map(int,input().split()))

tree = [None]*(N*4)
init(0,N-1,1)

for _ in range(Q):
    a,b,c = map(int,input().split())
    if a == 1:
        A[b-1] = c
        update(0,N-1,1,b-1)
    else:
        print(query(0,N-1,1,b-1,c-1)[2])