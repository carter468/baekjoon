# 불우이웃돕기
# Gold 3, MST

import heapq

n = int(input())
arr = [input() for _ in range(n)]

dic = {'0':0}
for i in range(26):
    dic[chr(i+97)] = i+1
    dic[chr(i+65)] = i+27

result = 0
graph = [[] for _ in range(n)]
for i in range(n):
    for j in range(n):
        result += dic[arr[i][j]]
        if i != j and arr[i][j] != '0':
            graph[i].append((dic[arr[i][j]],j))
            graph[j].append((dic[arr[i][j]],i))

count = 0
visited = [False]*n
q = [(0,0)]
while q:
    c,x = heapq.heappop(q)
    if visited[x]: continue
    visited[x] = True
    result -= c
    count += 1
    for nc,nx in graph[x]:
        heapq.heappush(q,(nc,nx))
print(result if count == n else -1)
