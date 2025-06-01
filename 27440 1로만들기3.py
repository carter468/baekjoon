# 1로 만들기 3
# Gold 4, BFS

from collections import deque

N = int(input())

q = deque([N])
visited = {N:0}
while q:
    x = q.popleft()
    if x == 1:
        print(visited[x])
        break

    if x%3 == 0 and x//3 not in visited:
        visited[x//3] = visited[x]+1
        q.append(x//3)
    
    if x%2 == 0 and x//2 not in visited:
        visited[x//2] = visited[x]+1
        q.append(x//2)
    
    if x-1 not in visited:
        visited[x-1] = visited[x]+1
        q.append(x-1)