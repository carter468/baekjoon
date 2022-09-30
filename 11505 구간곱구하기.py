# 구간 곱 구하기

import sys
input = sys.stdin.readline

def maketree(start,end,node):
    if start == end:
        tree[node] = num[start]
        return tree[node]
    mid = (start+end)//2
    tree[node] = maketree(start,mid,node*2)*maketree(mid+1,end,node*2+1)%1000000007
    return tree[node]

def ans(start,end,node,left,right):
    if left > end or right < start:
        return 1
    if left <= start and end <= right:
        return tree[node]
    mid = (start+end)//2
    return ans(start,mid,node*2,left,right)*ans(mid+1,end,node*2+1,left,right)%1000000007

def update(start,end,node,idx,c):
    if idx < start or idx > end:
        return
    if start == end:
        tree[node] = c
        return 
    mid = (start+end)//2
    update(start,mid,node*2,idx,c)
    update(mid+1,end,node*2+1,idx,c)
    tree[node] = tree[node*2] * tree[node*2+1] % 1000000007

n,m,k = map(int,input().split())
num = []
for _ in range(n):
    num.append(int(input()))
tree = [1]*(n*4)
maketree(0,n-1,1)
for _ in range(m+k):
    a,b,c = map(int,input().split())
    if a==1:
        update(0,n-1,1,b-1,c)
        num[b-1] = c
    else:
        print(ans(0,n-1,1,b-1,c-1))