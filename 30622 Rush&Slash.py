# Rush & Slash
# Gold 2, disjoint set

import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

n = int(input())
arr = [tuple(map(int,input().split())) for _ in range(n)]

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

dic = {}
parent = list(range(n))
for i in range(n):
    x,y = arr[i]
    dic[(x,y)] = i
    for nx,ny in (x,y+1),(x,y-1),(x+1,y+1),(x+1,y),(x+1,y-1),(x-1,y+1),(x-1,y),(x-1,y-1):
        if (nx,ny) in dic:
            i = find(i)
            x1,y1 = arr[i]
            j = find(dic[(nx,ny)])
            x2,y2 = arr[j]
            if abs(x1)+abs(y1) < abs(x2)+abs(y2):
                parent[j] = i
            else:
                parent[i] = j

dist = []
for i in range(n):
    if find(i) == i:
        x,y = arr[i]
        dist.append(abs(x)+abs(y))

print(sum(dist)*2-max(dist))