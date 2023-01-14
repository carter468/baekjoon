# 공항
# Gold 2, 분리 집합

import sys
input = sys.stdin.readline

def find(x):
    if root[x] != x:
        root[x] = find(root[x])
    return root[x]

root = [i for i in range(int(input())+1)]
count = 0
for _ in range(int(input())):
    g = int(input())
    i = find(g)
    if i==0:
        break
    root[find(i)] = find(i-1)
    count += 1

print(count)