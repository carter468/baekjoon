# 가장 가까운 공통조상

import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    parent = [0]*(n+1)
    for _ in range(n-1):
        a,b = map(int,input().split())
        parent[b] = a
    
    a,b = map(int,input().split())
    ancestor = [a]
    while parent[a] != 0:
        ancestor.append(parent[a])
        a = parent[a]
    while True:
        if b in ancestor:
            print(b)
            break
        b = parent[b]