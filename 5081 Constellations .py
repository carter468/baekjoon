# Constellations 
# Gold 5, 분리집합

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

s = 1
while (n := int(input())):
    arr = [tuple(map(int,input().split())) for _ in range(n)]
    root = list(range(n))
    
    for i in range(n):
        m = [sys.maxsize]
        for j in range(n):
            if i != j:
                d = (arr[i][0]-arr[j][0])**2+(arr[i][1]-arr[j][1])**2
                if d < m[0]:
                    m = [d,[j]]
                elif d == m[0]:
                    m[1].append(j)
        for j in m[1]:
            union(i,j)

    count = 0
    for i in range(n):
        if find(i) == i: 
            count += 1
    print(f'Sky {s} contains {count} constellations.')
    s += 1