# Count Circle Groups
# Gold 4, union-find, geometry

import sys
input = sys.stdin.readline

def find(x):
    if root[x] != x:
        root[x] = find(root[x])
    return root[x]

def union(a,b):
    a,b = find(a),find(b)
    if a > b:
        root[a] = b
    else:
        root[b] = a

for _ in range(int(input())):
    n = int(input())
    arr = [tuple(map(int,input().split())) for _ in range(n)]

    root = list(range(n))
    for i in range(n):
        for j in range(i+1,n):
            if (arr[i][0]-arr[j][0])**2+(arr[i][1]-arr[j][1])**2 <= (arr[i][2]+arr[j][2])**2:
                union(i,j)

    count = 0
    for i in range(n):
        if find(i) == i: count += 1
    print(count)