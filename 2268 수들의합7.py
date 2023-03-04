# 수들의 합 7
# Gold 1, segtree

import sys
input = sys.stdin.readline

def update(start,end,node,index,num):
    if index<start or index>end: return
    if start==end:
        tree[node]=num
        return
    
    mid = (start+end)//2
    update(start,mid,node*2,index,num)
    update(mid+1,end,node*2+1,index,num)
    tree[node] = tree[node*2]+tree[node*2+1]

def query(start,end,left,right,node):
    if left>end or right<start: return 0
    if left<=start and end<=right: return tree[node]

    mid = (start+end)//2
    return query(start,mid,left,right,node*2)+query(mid+1,end,left,right,node*2+1)

n,m = map(int,input().split())
arr = [0]*n
tree = [0]*(4*n)
for _ in range(m):
    c,i,j = map(int,input().split())
    if c==0:
        if i>j:
            i,j = j,i
        print(query(0,n-1,i-1,j-1,1))
    else:
        update(0,n-1,1,i-1,j)