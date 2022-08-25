# 여행 가자

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def find(x):
    if root[x] != x:
        root[x] = find(root[x])
    return root[x]

def union(a,b):
    a1 = find(a)
    b1 = find(b)
    root[a] = a1
    root[b] = b1
    if a1 != b1:
        root[a1] = b1

n = int(input())
m = int(input())
root = [i for i in range(n+1)]
for i in range(n):
    c = list(map(int,input().split()))
    for j in range(i+1,n):
        if c[j] == 1:
            union(i+1,j+1)
plan = list(map(int,input().split()))

temp = find(plan[0])
answer = 'YES'
for i in range(1,n+1):
    find(i)
for x in plan[1:]:
    if root[x] != temp:
        answer = 'NO'
        break

print(answer)