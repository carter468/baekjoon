# 탈출
# Gold 4, BFS

from collections import deque

N,T,G = map(int,input().split())

q = deque([N])
visit = [-1]*10**5
visit[N] = 0
while q and visit[q[0]] <= T:
    x = q.popleft()
    if x == G:
        print(visit[x])
        break
    if x+1 < 10**5 and visit[x+1] == -1:
        visit[x+1] = visit[x]+1
        q.append(x+1)
    y = x*2-10**(len(str(x*2))-1)
    if y >= 0 and x*2 < 10**5 and visit[y] == -1:
        visit[y] = visit[x]+1
        q.append(y)
else:
    print('ANG')