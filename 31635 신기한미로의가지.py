# 신기한 미로의 가지
# Gold 4, ad hoc, constructive

import sys

n = int(input())

graph = [[] for _ in range(n+1)]
parent = [0]*(n+1)
parent[1] = -1
node = 1
count = n-1
while count:
    print('maze')
    sys.stdout.flush()
    k = int(input())
    if parent[k] == 0:
        graph[node].append(k)
        parent[k] = node
        count -= 1
        node = k
    elif parent[k] == node:
        print('gaji',node)
        sys.stdout.flush()
        input()
        print('gaji',parent[node])
        sys.stdout.flush()
        input()
        node = parent[node]
    else: node = k

print('answer')
for i in range(1,n+1):
    for j in graph[i]:
        print(i,j)