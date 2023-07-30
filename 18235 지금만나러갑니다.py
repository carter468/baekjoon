# 지금 만나러 갑니다
# Gold 3, BFS

from collections import deque

n,a,b = map(int,input().split())

q = deque([(a,0)])
visit = [[] for _ in range(n+1)]
while q:
    x,d = q.popleft()
    for nx in (x+2**d,x-2**d):
        if 0 < nx <= n:
            visit[nx].append(d+1)
            q.append((nx,d+1))

q = deque([(b,0)])
while q:
    x,d = q.popleft()
    if d in visit[x]:
        print(d)
        break

    for nx in (x+2**d,x-2**d):
        if 0 < nx <= n:
            q.append((nx,d+1))
else:
    print(-1)