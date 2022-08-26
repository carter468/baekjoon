# 친구네트워크

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
    if a != b:
        root[a] = root[b]
        cnt[b] += cnt[a]

t = int(input())
for _ in range(t):
    f = int(input())
    root = dict()           # 루트가 누구인지
    cnt = dict()            # 친구수가 몇명인지
    for _ in range(f):
        a,b = map(str,input().split())
        if a not in root:
            root[a] = a
            cnt[a] = 1
        if b not in root:
            root[b] = b
            cnt[b] = 1
        if root[a] != root[b]:
            union(a,b) 
        print(cnt[find(b)])