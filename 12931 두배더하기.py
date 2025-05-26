# 두 배 더하기
# Gold 5, BFS

from collections import deque
M = 1001

m1,m2 = 0,0
input()
for t in map(int,input().split()):
    visited = [False]*M
    visited[0] = True
    q = deque([(0,0,0)])
    while q:
        x,a,b = q.popleft()
        if x == t: break
        if x*2 < M and not visited[x*2]:
            visited[x*2] = True
            q.append((x*2,a,b+1))
        if x+1 < M and not visited[x+1]:
            visited[x+1] = True
            q.append((x+1,a+1,b))
    m1 += a
    m2 = max(m2,b)
print(m1+m2)