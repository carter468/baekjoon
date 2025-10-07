# 수열과 쿼리
# Gold 1, disjoint set

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
MAX = 300001

def find(x):
    if root[x] != x:
        root[x] = find(root[x])
    return root[x]

N = int(input())
A = list(map(int,input().split()))

root = list(range(N))
idx = [-1]*MAX
for i,a in enumerate(A):
    if idx[a] == -1:
        idx[a] = i
    else:
        root[i] = idx[a]

for _ in range(int(input())):
    q = tuple(map(int,input().split()))
    if q[0] == 1:
        x,y = q[1:]
        if idx[x] != -1:
            if idx[y] == -1:
                idx[y] = idx[x]
                A[idx[y]] = y
            else:
                root[idx[x]] = idx[y]
            idx[x] = -1
    elif q[0] == 2:
        z = q[1]-1
        print(A[find(z)])