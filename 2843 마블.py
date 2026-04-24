# 마블
# Platinum 3, offline query, disjoint set

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def find(x):
    if root[x] == -1: return -1
    if root[x] != x:
        root[x] = find(root[x])
    return root[x]

N = int(input())
E = [0]+list(map(int,input().split()))
query = [tuple(map(int,input().split())) for _ in range(int(input()))]

s = set()
for a,b in query:
    if a == 2: s.add(b)

root = list(range(N+1))
for i in range(1,N+1):
    j = find(E[i])
    if j != 0 and i not in s:
        root[i] = j
        if j == i: root[j] = -1

result = []
while query:
    q,i = query.pop()
    if q == 1:
        i = find(i)
        if i == -1: result.append('CIKLUS')
        else: result.append(i)
    else:
        j = find(E[i])
        root[i] = j
        if j == i: root[j] = -1

print(*result[::-1],sep='\n')