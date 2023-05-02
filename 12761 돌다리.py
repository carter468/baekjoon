# 돌다리
# Silver 1, BFS

from collections import deque
MAX = 100001

a,b,n,m = map(int,input().split())
visit = [0]*MAX
q = deque([n])
while 1:
    x = q.popleft()
    if x == m:
        print(visit[x])
        break
    for nx in (x+1,x-1,x+a,x-a,x+b,x-b,x*a,x*b):
        if nx < 0 or nx >= MAX or visit[nx]: continue
        visit[nx] = visit[x]+1
        q.append(nx)