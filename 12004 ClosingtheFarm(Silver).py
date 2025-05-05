# Closing the Farm (Silver)
# Gold 4, disjoint set

import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

def find(x):
    if root[x] != x:
        root[x] = find(root[x])
    return root[x]

N,M = map(int,input().split())
arr = [tuple(map(int,input().split())) for _ in range(M)]

closed = set()
for _ in range(N-1):
    root = list(range(N+1))
    narr = []
    for a,b in arr:
        if a in closed or b in closed: continue
        narr.append((a,b))
        a,b = find(a),find(b)
        root[a] = b
        k = b
    
    for i in range(1,N+1):
        if i not in closed and find(i) != k:
            print('NO')
            break
    else: print('YES')
    closed.add(int(input()))
    arr = narr
print('YES')