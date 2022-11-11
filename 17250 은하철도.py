# 17250 은하철도.py
# Gold 4, 분리집합

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n,m = map(int,input().split())
array = [0]
for _ in range(n):
    array.append(int(input()))

def find(x):
    if root[x] != x:
        root[x] = find(root[x])
    return root[x]

def union(x,y):
    x = find(x)
    y = find(y)
    if x<y:
        root[y] = x
        array[x] += array[y]
    elif x>y:
        root[x] = y
        array[y] += array[x]
    print(array[min(x,y)])

root = [i for i in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    union(a,b)