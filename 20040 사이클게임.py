# 사이클게임

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def find(x):
    if x != root[x]:
        root[x] = find(root[x])
    return root[x]

def union(a,b):
    a = find(a)
    b = find(b)
    if a==b:
        return True
    root[a] = b
    return False

n,m = map(int,input().split())
root = [i for i in range(n)]
for i in range(1,m+1):
    a,b = map(int,input().split())
    if union(a,b):
        print(i)
        break
else:
    print(0)