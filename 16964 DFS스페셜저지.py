# DFS 스페셜 저지
# Gold 3, DFS

import sys
input = sys.stdin.readline

n = int(input())
graph = [set() for _ in range(n+1)]
for _ in range(n-1):
    a,b = map(int,input().split())
    graph[a].add(b)
    graph[b].add(a)
graph[0].add(1)
graph[1].add(0)
arr = tuple(map(int,input().split()))

q = [0]
i = 0
while i < n:
    x = q[-1]
    while not graph[x]:
        q.pop()
        x = q[-1]
    if arr[i] in graph[x]:
        q.append(arr[i])
        graph[x].remove(arr[i])
        graph[arr[i]].remove(x)
    else:
        print(0)
        break
    i += 1
else: print(1)