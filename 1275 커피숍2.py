# 커피숍2
# Gold 1, fenwick tree

import sys
input = sys.stdin.readline

def prefix_sum(i):
    result = 0
    while i > 0:
        result += tree[i]
        i -= (i&-i)
    return result

def update(i,dif):
    while i <= N:
        tree[i] += dif
        i += (i&-i)

N,Q = map(int,input().split())
arr = list(map(int,input().split()))
tree = [0]*(N+1)
for i,x in enumerate(arr):
    update(i+1,x)

for _ in range(Q):
    x,y,a,b = map(int,input().split())
    if x > y: x,y = y,x
    print(prefix_sum(y)-prefix_sum(x-1))
    update(a,b-arr[a-1])
    arr[a-1] = b