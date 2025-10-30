# Arctic Network
# Gold 3, MST

import sys
input = sys.stdin.readline

def dist(i,j):
    x1,y1 = arr[i]
    x2,y2 = arr[j]
    return (x1-x2)**2+(y1-y2)**2

def find(x):
    if root[x] != x:
        root[x] = find(root[x])
    return root[x]

for _ in range(int(input())):
    S,P = map(int,input().split())
    arr = [tuple(map(int,input().split())) for _ in range(P)]
    if S >= P:
        print('0.00')
        continue

    edge = []
    for i in range(P):
        for j in range(i+1,P):
            edge.append((dist(i,j),i,j))
    edge.sort()

    root = list(range(P))
    count = 0
    for d,i,j in edge:
        i,j = find(i),find(j)
        if i != j:
            root[i] = j
            count += 1
            if count+S == P:
                print(f'{d**0.5+1e-9:.2f}')
                break