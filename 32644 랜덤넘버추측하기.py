# 랜덤 넘버 추측하기
# Gold 1, segtree

def maketree(start,end,node):
    if start == end:
        tree[node] = num[start]
        return tree[node]
    mid = (start+end)//2
    tree[node] = maketree(start,mid,node*2)+maketree(mid+1,end,node*2+1)
    return tree[node]

def ans(start,end,node,left,right):
    if left > end or right < start:
        return 0
    if left <= start and end <= right:
        return tree[node]
    mid = (start+end)//2
    return ans(start,mid,node*2,left,right)+ans(mid+1,end,node*2+1,left,right)

def update(start,end,node,idx,d):
    if idx < start or idx > end:
        return
    tree[node] -= d
    if start == end:
        return
    mid = (start+end)//2
    update(start,mid,node*2,idx,d)
    update(mid+1,end,node*2+1,idx,d)
    
n,m = map(int,input().split())
num = tuple(map(int,input().split()))

tree = [0]*(n*4)
maketree(0,n-1,1)
for a in map(int,input().split()):
    print(ans(0,n-1,1,0,a-1),end=' ')
    update(0,n-1,1,a-1,num[a-1])