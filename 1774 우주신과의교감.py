# 우주신과의 교감

import sys
input = sys.stdin.readline

def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]

n,m = map(int,input().split())
parent = [i for i in range(n+1)]
god = []        # 우주신들의 좌표
for _ in range(n):
    god.append(list(map(int,input().split())))
edge = []       # [거리,번호,번호]
for _ in range(m):
    edge.append([0]+list(map(int,input().split())))     # 이미 연결된 우주신들은 거리가 0

for i in range(n):
    for j in range(i+1,n):
        cost = ((god[i][0]-god[j][0])**2 + (god[i][1]-god[j][1])**2)**0.5
        edge.append([cost,i+1,j+1])             # 거리계산

edge.sort()         # 거리를 기준으로 정렬

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

print('{:.2f}'.format(ans))