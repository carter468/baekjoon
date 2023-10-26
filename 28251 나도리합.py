# 나도리합
# Gold 3, math, disjoint set

import sys
input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a,b):
    a,b = find(a),find(b)
    if a == b: return power[a]
    if a > b: a,b = b,a
    parent[b] = a
    power[a] += power[b]+size[a]*size[b]
    size[a] += size[b]
    return power[a]
    
n,q = map(int,input().split())
size = list(map(int,input().split()))
power = [0]*n
parent = list(range(n))

for _ in range(q):
    a,b = map(int,input().split())
    print(union(a-1,b-1))