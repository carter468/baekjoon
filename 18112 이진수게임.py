# 이진수 게임
# Gold 5, bitmask, BFS

from collections import deque

l,k = input(),input()

a,b = 0,0
for i,x in enumerate(l[::-1]):
    if x == '1':
        a += 1<<i
for i,x in enumerate(k[::-1]):
    if x == '1':
        b += 1<<i

visited = [-1]*1024
visited[a] = 0
q = deque([a])
while q:
    x = q.popleft()
    if x == b:
        print(visited[x])
        break
    if x < 1023 and visited[x+1] == -1:
        visited[x+1] = visited[x]+1
        q.append(x+1)
    if x > 0 and visited[x-1] == -1:
        visited[x-1] = visited[x]+1
        q.append(x-1)
    for i in range(len(bin(x))-3):
        if (x>>i)&1 == 1: nx = x-(1<<i)
        else: nx = x+(1<<i)
        if visited[nx] == -1:
            visited[nx] = visited[x]+1
            q.append(nx)