# Balanced Lineup
# Gold 1, segment tree

import sys
input = sys.stdin.readline

def maketree(start,end,node):
    if start == end:
        tree[node] = h[end],h[end]
        return tree[node]
    mid = (start+end)//2
    a,b = maketree(start,mid,node*2)
    c,d = maketree(mid+1,end,node*2+1)
    tree[node] = min(a,c),max(b,d)
    return tree[node]

def query(start,end,node,left,right):
    if left > end or right < start: return 10**6,1
    if left <= start and end <= right: return tree[node]
    mid = (start+end)//2
    a,b = query(start,mid,node*2,left,right)
    c,d = query(mid+1,end,node*2+1,left,right)
    return min(a,c),max(b,d)

n,q = map(int,input().split())
h = [int(input()) for _ in range(n)]

tree = [0]*(n*4)
maketree(0,n-1,1)
for _ in range(q):
    a,b = map(int,input().split())
    c,d = query(0,n-1,1,a-1,b-1)
    print(d-c)