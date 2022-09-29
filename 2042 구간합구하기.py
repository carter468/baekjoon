# 구간 합 구하기

import sys
input = sys.stdin.readline

def maketree(start,end,node):
    if start == end:
        tree[node] = num[start]
        return tree[node]
    mid = (start+end)//2
    tree[node] = maketree(start,mid,node*2) + maketree(mid+1,end,node*2+1)
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
    tree[node] += d
    if start == end:
        return
    mid = (start+end)//2
    update(start,mid,node*2,idx,d)
    update(mid+1,end,node*2+1,idx,d)

n,m,k = map(int,input().split())
num = []
for _ in range(n):
    num.append(int(input()))
tree = [0]*(n*4)
maketree(0,n-1,1)

for _ in range(m+k):
    a,b,c = map(int,input().split())
    if a==1:
        d = c-num[b-1]
        num[b-1] = c
        update(0,n-1,1,b-1,d)
    else:
        print(ans(0,n-1,1,b-1,c-1))
    