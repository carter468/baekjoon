# 전국시대
# Gold 4, disjoint set

import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

n,m = map(int,input().split())
army = [int(input()) for _ in range(n)]

parent = list(range(n))

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

for _ in range(m):
    o,p,q = map(int,input().split())
    p,q = find(p-1),find(q-1)
    if o == 1:
        parent[q] = p
        army[p] += army[q]
        army[q] = 0
    else:
        if army[p] == army[q]:
            army[p],army[q] = 0,0
        elif army[p] > army[q]:
            parent[q] = p
            army[p] -= army[q]
            army[q] = 0
        else:
            parent[p] = q
            army[q] -= army[p]
            army[p] = 0

result = []
for a in army:
    if a != 0: result.append(a)
print(len(result))
if result: print(*sorted(result))