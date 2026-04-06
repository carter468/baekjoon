# 쉽고 간단한 문제
# Gold 1, DP, segtree, coordinate compression

def query(start,end,node,left,right):
    if left > end or right < start:
        return 0
    if left <= start and end <= right:
        return tree[node]
    mid = (start+end)//2
    return max(query(start,mid,node*2,left,right),query(mid+1,end,node*2+1,left,right))

def update(start,end,node,idx,v):
    if idx < start or idx > end:
        return tree[node]
    if start == end:
        tree[node] = v
        return v
    mid = (start+end)//2
    tree[node] = max(update(start,mid,node*2,idx,v),update(mid+1,end,node*2+1,idx,v))
    return tree[node]

N = int(input())
A = tuple(map(int,input().split()))

dic = {a:i for i,a in enumerate(sorted(set(A)))}
tree = [0]*(N*4)

for a in A:
    if a-1 in dic:
        x1 = dic[a-1]
        y1 = query(0,N-1,1,x1,x1)
        update(0,N-1,1,x1,0)
    if a+1 in dic:
        x2 = dic[a+1]
        y2 = query(0,N-1,1,x2,x2)
        update(0,N-1,1,x2,0)
    
    update(0,N-1,1,dic[a],tree[1]+1)
    if a-1 in dic:
        update(0,N-1,1,x1,y1)
    if a+1 in dic:
        update(0,N-1,1,x2,y2)

print(tree[1])