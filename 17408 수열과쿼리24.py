# 수열과 쿼리 24
# Platinum 4, segtree

import sys
input = sys.stdin.readline

def init(start,end,node):
    if start == end:
        tree[node] = [A[start],0]
        return tree[node]
    mid = (start+end)//2
    arr = init(start,mid,node*2)+init(mid+1,end,node*2+1)
    tree[node] = sorted(arr)[2:]
    return tree[node]

def query(start,end,node,left,right):
    if left > end or right < start:
        return [0,0]
    if left <= start and end <= right:
        return tree[node]
    mid = (start+end)//2
    arr = query(start,mid,node*2,left,right)+query(mid+1,end,node*2+1,left,right)
    return sorted(arr)[2:]

def update(start,end,node,idx,v):
    if idx < start or idx > end:
        return tree[node]
    if start == end:
        if start == idx:
            tree[node] = [v,0]
        return tree[node]
    
    mid = (start+end)//2
    arr = update(start,mid,node*2,idx,v)+update(mid+1,end,node*2+1,idx,v)
    tree[node] = sorted(arr)[2:]
    return tree[node]

N = int(input())
A = tuple(map(int,input().split()))

tree = [[0,0] for _ in range(N*4)]
init(0,N-1,1)
for _ in range(int(input())):
    q = tuple(map(int,input().split()))
    if q[0] == 1:
        i,v = q[1:]
        update(0,N-1,1,i-1,v)
    else:
        l,r = q[1:]
        print(sum(query(0,N-1,1,l-1,r-1)))