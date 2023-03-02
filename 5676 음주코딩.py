# 음주 코딩
# Gold 1, segtree

import sys
input = sys.stdin.readline

def sign(n):
    return 0 if n==0 else n//abs(n)

class SegmentTree:
    def __init__(self,arr):
        self.arr = arr
        self.tree = [0]*(4*n)
        self.init_tree(1,0,n-1)

    def init_tree(self,node,start,end):
        if start==end:
            self.arr[start] = sign(self.arr[start])
            self.tree[node] = self.arr[start]
            return self.tree[node]

        mid = (start+end)//2
        self.tree[node] = self.init_tree(node*2,start,mid)*self.init_tree(node*2+1,mid+1,end)
        return self.tree[node]
    
    def update(self,node,start,end,index,change):
        if index<start or index>end: return
        if start==end:
            self.tree[node] = change
            return

        mid = (start+end)//2
        self.update(node*2,start,mid,index,change)
        self.update(node*2+1,mid+1,end,index,change)
        self.tree[node] = self.tree[node*2]*self.tree[node*2+1]

    def query(self,node,start,end,left,right):
        if left>end or right<start:
            return 1

        if left<=start and end<=right:
            return self.tree[node]

        mid = (start+end)//2
        return self.query(node*2,start,mid,left,right)*self.query(node*2+1,mid+1,end,left,right)
    
while 1:
    try: n,k = map(int,input().split())
    except: break

    st = SegmentTree(list(map(int,input().split())))
    for _ in range(k):
        c = input().split()
        i,j = map(int,c[1:])
        if c[0]=='C':
            if st.arr[i-1] != (a:=sign(j)):
                st.arr[i-1] = a
                st.update(1,0,n-1,i-1,a)
        else:
            print(['0','+','-'][st.query(1,0,n-1,i-1,j-1)],end='')
    print()