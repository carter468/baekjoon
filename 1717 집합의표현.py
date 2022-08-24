# 집합의 표현

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def find(x):
    if root[x] != x:
        root[x] = find(root[x])
    return root[x]

def union(a,b):
    a1 = find(a)
    b1 = find(b)
    root[a] = a1
    root[b] = b1
    if a1 != b1:
        root[a1] = b1

n,m = map(int,input().split())
root = [i for i in range(n+1)]

for _ in range(m):
    c,a,b = map(int,input().split())
    if c == 0:
        union(a,b)
    else:
        if find(a) == find(b):
            print('YES')
        else:
            print('NO')