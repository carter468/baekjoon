# 여러분의 다리가 되어드리겠습니다!
# Gold 5, 분리 집합

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def find(x):
    if root[x] != x:
        root[x] = find(root[x])
    return root[x]
def union(x,y):
    x1,y1=find(x),find(y)
    if x1!=y1:
        root[x1] = y1

n = int(input())
root = [i for i in range(n+1)]
for _ in range(n-2):
    a,b = map(int,input().split())
    union(a,b)
for i in range(1,n+1):
    for j in range(i+1,n+1):
        if find(i)!=find(j):
            print(i,j)
            quit()