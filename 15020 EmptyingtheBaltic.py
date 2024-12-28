# Emptying the Baltic
# Gold 2, BFS, priority queue

import sys,heapq
input = sys.stdin.readline

h,w = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(h)]
i,j = map(int,input().split())

i,j = i-1,j-1
q = [(arr[i][j],i,j)]
visited = [[False]*w for _ in range(h)]
visited[i][j] = True
answer = 0
while q:
    d,x,y = heapq.heappop(q)
    answer -= d
    for nx,ny in (x+1,y),(x+1,y+1),(x+1,y-1),(x,y+1),(x,y-1),(x-1,y+1),(x-1,y),(x-1,y-1):
        if 0 <= nx < h and 0 <= ny < w:
            arr[nx][ny] = max(arr[nx][ny],d)
            if arr[nx][ny] < 0 and not visited[nx][ny]:
                heapq.heappush(q,(arr[nx][ny],nx,ny))
                visited[nx][ny] = True
print(answer)