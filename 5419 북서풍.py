# 북서풍

import sys
input = sys.stdin.readline

def coor_comp():  # 좌표압축
    island.sort(key = lambda x:x[1])
    rank = -1
    prev = 10**10
    for i in range(n):
        if island[i][1] != prev:
            rank += 1
        prev = island[i][1]
        island[i][1] = rank
    island.sort(key = lambda x:[x[0],-x[1]])
def update(node,left,right,idx):
    if left == right:
        tree[node] += 1
        return
    mid = (left+right)//2
    if idx<=mid:
        update(node*2,left,mid,idx)
    else:
        update(node*2+1,mid+1,right,idx)
    tree[node] = tree[node*2]+tree[node*2+1]
def query(node,left,right,start,end):
    if right<start or left>end:
        return 0
    if left<=start and right>=end:
        return tree[node]
    mid = (start+end)//2
    return query(node*2,left,right,start,mid)+query(node*2+1,left,right,mid+1,end)

t = int(input())
for _ in range(t):
    island = []
    n = int(input())
    for _ in range(n):
        island.append(list(map(int,input().split())))
    coor_comp()
    tree = [0]*n*4
    ans = 0
    for i in range(n):
        ans += query(1,island[i][1],n-1,0,n-1)
        update(1,0,n-1,island[i][1])
    print(ans)