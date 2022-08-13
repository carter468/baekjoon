# 별자리만들기

import sys
input = sys.stdin.readline

def find(x):
    if x != root[x]:
        root[x] = find(root[x])
    return root[x]

n = int(input())
star = []
for _ in range(n):
    star.append(list(map(float,input().split())))

root = [i for i in range(n+1)]
data = []
for i in range(n):
    for j in range(i+1,n):
        data.append([i,j,((star[i][0]-star[j][0])**2 + (star[i][1]-star[j][1])**2)**0.5])
data.sort(key=lambda x:x[2])

ans = 0
for a,b,c in data:
    ra = find(a)
    rb = find(b)
    if ra != rb:
        if ra > rb:
            root[ra] = rb
        else:
            root[rb] = ra
        ans += c

print(round(ans,2))