# Tinted Glass Window
# Gold 1, prefix sum, coordinate compression

import sys
input = sys.stdin.readline

N = int(input())
T = int(input())
arr = [tuple(map(int,input().split())) for _ in range(N)]

x,y = set(),set()
for x1,y1,x2,y2,_ in arr:
    x.update((x1,x2))
    y.update((y1,y2))
x,y = sorted(x),sorted(y)
lx,ly = len(x),len(y)

dic_x,dic_y = dict(),dict()
for i in range(lx):
    dic_x[x[i]] = i
for j in range(ly):
    dic_y[y[j]] = j

imos = [[0]*ly for _ in range(lx)]
for x1,y1,x2,y2,t in arr:
    x1,y1,x2,y2 = dic_x[x1],dic_y[y1],dic_x[x2],dic_y[y2]
    imos[x1][y1] += t
    imos[x1][y2] -= t
    imos[x2][y1] -= t
    imos[x2][y2] += t

for i in range(lx):
    for j in range(1,ly):
        imos[i][j] += imos[i][j-1]
for j in range(ly):
    for i in range(1,lx):
        imos[i][j] += imos[i-1][j]

result = 0
for i in range(lx):
    for j in range(ly):
        if imos[i][j] >= T:
            result += (x[i+1]-x[i])*(y[j+1]-y[j])
print(result)