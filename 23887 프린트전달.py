# 프린트 전달
# Gold 2, BFS, DP

from collections import deque
import sys,heapq
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

def dfs(node):
    dp[node] = 1
    for nxt in graph[node]:
        dfs(nxt)
        dp[node] += dp[nxt]

N,M,K = map(int,input().split())
point = [0]*(K+1)
grid = [[0]*(M+1) for _ in range(N+1)]
for i in range(K):
    x,y = map(int,input().split())
    grid[x][y] = i+1
    point[i+1] = (x,y)
S = int(input())

graph = [[] for _ in range(K+1)]
visited = [False]*(K+1)
visited[S] = True
q = deque([S])
while q:
    l = len(q)
    child = []
    for _ in range(l):
        num = q.popleft()
        x,y = point[num]
        for nx,ny in (x+1,y),(x+1,y+1),(x+1,y-1),(x,y+1),(x,y-1),(x-1,y+1),(x-1,y),(x-1,y-1):
            if 1 <= nx <= N and 1 <= ny <= M and grid[nx][ny] and not visited[grid[nx][ny]]:
                visited[grid[nx][ny]] = True
                graph[num].append(grid[nx][ny])
                heapq.heappush(child,grid[nx][ny])
    while child:
        q.append(heapq.heappop(child))

dp = [0]*(K+1)
dfs(S)
answer = []
for i in range(1,K+1):
    if dp[i] == 0:
        answer = [-1]
        break
    answer.append(dp[i])
print(*answer)