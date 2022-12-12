# 소셜 네트워킹 어플리케이션
# Gold 5, 분리 집합

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def find(x):
    if root[x] != x:
        root[x] = find(root[x])
    return root[x]

def union(x,y):
    rx,ry = find(x),find(y)
    if rx!=ry:
        root[rx] = ry

for i in range(int(input())):
    print(f'Scenario {i+1}:')
    n = int(input())    # 유저수
    k = int(input())    # 관계수
    root = [i for i in range(n+1)]
    for _ in range(k):
        a,b = map(int,input().split())
        union(a,b)
    
    m = int(input())    # 쿼리수
    for _ in range(m):
        a,b = map(int,input().split())
        print(1 if find(a)==find(b) else 0)
    print()