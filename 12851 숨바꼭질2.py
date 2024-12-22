# 숨바꼭질 2
# Gold 4, BFS

from collections import deque

N,K = map(int,input().split())

visited = [[-1,0] for _ in range(100001)]
visited[N] = [0,1]
q = deque([N])
while q:
    x = q.popleft()
    for nx in (x+1,x-1,x+x):
        if 0 <= nx <= 10**5:
            if visited[nx][0] == -1:
                visited[nx] = [visited[x][0]+1,visited[x][1]]
                q.append(nx)
            elif visited[nx][0] == visited[x][0]+1:
                visited[nx][1] += visited[x][1]
print(*visited[K],sep='\n')