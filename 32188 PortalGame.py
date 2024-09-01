# Portal Game
# Gold 4, dijkstra

import sys,heapq
input = sys.stdin.readline

n,c = map(int,input().split())
arr = [0]*n
for _ in range(c):
    t,a,b = map(int,input().split())
    arr[a] = (t,b)
q = [(0,0)]
visited = [10**9]*n
visited[0] = 0
while q:
    d,x = heapq.heappop(q)
    if x == n-1:
        print(d)
        break
    if arr[x] == 0:
        if d+1 < visited[x+1]:
            visited[x+1] = d+1
            heapq.heappush(q,(d+1,x+1))
    else:
        nx = arr[x][1]
        if d < visited[nx]:
            visited[nx] = d
            heapq.heappush(q,(d,nx))
        if arr[x][0] == 1 and d+1 < visited[x+1]:
            visited[x+1] = d+1
            heapq.heappush(q,(d+1,x+1))
else: print(-1)
