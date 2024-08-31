# 연락
# Gold 2, disjoint set, combinatorics

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def find(x):
    if root[x] != x:
        root[x] = find(root[x])
    return root[x]

n,m = map(int,input().split())
c = tuple(map(int,input().split()))
count = [[0,0] for _ in range(n+1)]
for i,p in enumerate(c):
    count[i+1][p%2] = 1
root = list(range(n+1))
result = 0
for _ in range(m):
    a,b = map(int,input().split())
    a,b = find(a),find(b)
    if a != b:
        if a > b: a,b = b,a
        root[b] = a
        result -= count[a][0]*count[a][1]+count[b][0]*count[b][1]
        count[a][0] += count[b][0]
        count[a][1] += count[b][1]
        result += count[a][0]*count[a][1]
    print(result)
