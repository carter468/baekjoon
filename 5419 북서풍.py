# 북서풍
# Platinum 3, segtree, sweeping, coordinate compression

import sys
input = sys.stdin.readline

def update(start,end,node,idx):
    if idx < start or end < idx: return
    tree[node] += 1
    if start == end: return
    mid = (start+end)>>1
    update(start,mid,node*2,idx)
    update(mid+1,end,node*2+1,idx)

def answer(start,end,node,left,right):
    if end < left or right < start: return 0
    if left <= start and end <= right: return tree[node]
    mid = (start+end)>>1
    return answer(start,mid,node*2,left,right)+answer(mid+1,end,node*2+1,left,right)

for _ in range(int(input())):
    arr = sorted([tuple(map(int,input().split())) for _ in range(int(input()))],key=lambda x:(-x[1],x[0]))
    
    arr_x = []
    for x,y in arr:
        arr_x.append(x)
    arr_x = sorted(set(arr_x))
    dic = {}
    n = len(arr_x)
    for i in range(n):
        dic[arr_x[i]] = i

    tree = [0]*(n*4)
    count = 0
    for x,y in arr:
        count += answer(0,n-1,1,0,dic[x])
        update(0,n-1,1,dic[x])

    print(count)

import sys
input = sys.stdin.readline

def update(i):
    while i <= n:
        tree[i] += 1
        i += (i&-i)

def answer(i):
    result = 0
    while i > 0:
        result += tree[i]
        i -= (i&-i)
    return result

for _ in range(int(input())):
    arr = sorted([tuple(map(int,input().split())) for _ in range(int(input()))],key=lambda x:(-x[1],x[0]))

    arr_x = []
    for x,y in arr:
        arr_x.append(x)
    arr_x = sorted(set(arr_x))
    dic = {}
    n = len(arr_x)
    for i in range(n):
        dic[arr_x[i]] = i+1

    tree = [0]*(n+1)
    count = 0
    for x,y in arr:
        count += answer(dic[x])
        update(dic[x])
    print(count)