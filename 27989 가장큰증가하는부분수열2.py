# 가장 큰 증가하는 부분 수열 2
# Platinum 5, segtree

def query(start,end,node,left,right):
    if left > end or right < start:
        return 0
    if left <= start and end <= right:
        return tree[node]
    mid = (start+end)//2
    return max(query(start,mid,node*2,left,right),query(mid+1,end,node*2+1,left,right))

def update(start,end,node,idx,x):
    if idx < start or idx > end: return

    tree[node] = max(tree[node],x)
    if start == end: return
    
    mid = (start+end)//2
    update(start,mid,node*2,idx,x)
    update(mid+1,end,node*2+1,idx,x)

N = int(input())
A = sorted([(i,a) for i,a in enumerate(map(int,input().split()))],key=lambda x:(x[1],-x[0]))

tree = [0]*(N*4)
for i,a in A:
    update(0,N-1,1,i,query(0,N-1,1,0,i-1)+a)
print(tree[1])