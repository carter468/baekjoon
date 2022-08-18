# 행성터널

import sys
input = sys.stdin.readline

def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]

n = int(input())
planet = []
for i in range(n):
    planet.append(list(map(int,input().split()))+[i])

edge = []
for i in range(3):
    planet.sort(key=lambda x:x[i])
    for j in range(1,n):
        edge.append([abs(planet[j-1][i]-planet[j][i]),planet[j-1][3],planet[j][3]])
parent = [i for i in range(n+1)]
edge.sort()

ans = 0
for cost,a,b in edge:   #kruskal 알고리즘
    roota = find(a)
    rootb = find(b)
    if roota != rootb:
        if roota > rootb:
            parent[roota] = rootb
        else:
            parent[rootb] = roota
        ans += cost

print(ans)