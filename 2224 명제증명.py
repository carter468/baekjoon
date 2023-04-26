# 명제 증명
# Gold 4, Floyd-Warshall

import sys
input = sys.stdin.readline
M = 58

count = 0
graph = [[0]*M for _ in range(M)]
for _ in range(int(input())):
    a = input()
    p,q = ord(a[0])-65,ord(a[5])-65
    if p == q or graph[p][q]: continue
    graph[p][q] = 1
    count += 1

for k in range(M):
    for i in range(M):
        for j in range(M):
            if graph[i][j] or i == j: continue
            graph[i][j] = graph[i][k] and graph[k][j]
            if graph[i][j]:
                count += 1
            
print(count)
for i in range(M):
    for j in range(M):
        if graph[i][j]:
            print(chr(i+65),'=>',chr(j+65))