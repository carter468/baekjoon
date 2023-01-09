# BFS 스페셜 저지
# Gold 3, 너비 우선 탐색

from collections import deque
import sys
input = sys.stdin.readline

def solve():
    visit = [False]*(N+1)
    q = deque([1])
    visit[1] = True

    idx = 1
    while q:
        x = q.popleft()
        children = []
        for child in graph[x]:
            if not visit[child]:
                visit[child] = True
                children.append(child)
        
        l = len(children)
        temp = order[idx:idx+l]
        if set(temp) == set(children):
            q.extend(temp)
            idx += l
        else:
            return 0
    return 1

N = int(input())
graph = [[] for _ in range(N+1)]
visit = [False]*(N+1)
for _ in range(N-1):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
order = tuple(map(int,input().split()))

if order[0] == 1:
    print(solve())
else:
    print(0)