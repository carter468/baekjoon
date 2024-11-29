# Rectangle Coloring
# Gold 5, disjoint set

import sys
input = sys.stdin.readline

def find(x):
    if root[x] != x:
        root[x] = find(root[x])
    return root[x]

for _ in range(int(input())):
    N = int(input())
    arr = [tuple(map(int,input().split())) for _ in range(N)]

    root = list(range(N))
    for i in range(N):
        for j in range(i+1,N):
            x1,y1,x2,y2 = arr[i]
            x3,y3,x4,y4 = arr[j]
            if ((x3 <= x1 <= x4 or x1 <= x3 <= x2) and (y3 <= y1 <= y4 or y1 <= y3 <= y2)):
                root[find(i)] = find(j)
    
    result = 0
    for i in range(N):
        if find(i) == i: result += 1
    print(result)