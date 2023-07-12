# 등수 찾기
# Gold 3, BFS

from collections import deque
import sys
input = sys.stdin.readline

def bfs(s,arr):
    result = 0
    q = deque([s])
    visit = [0]*(n+1)
    visit[s] = 1
    while q:
        x = q.popleft()
        for nx in arr[x]:
            if not visit[nx]:
                q.append(nx)
                visit[nx] = 1
                result += 1
    return result

n,m,x = map(int,input().split())
a1 = [[] for _ in range(n+1)]
a2 = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    a1[a].append(b)
    a2[b].append(a)

print(1+bfs(x,a2),n-bfs(x,a1))