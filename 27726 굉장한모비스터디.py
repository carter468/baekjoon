# 굉장한 모비스터디
# Gold 1, DFS, hash_set

from collections import defaultdict
import sys
input = sys.stdin.readline

N = int(input())
M1,M2,M3 = map(int,input().split())

graph = [[[] for _ in range(N+1)] for _ in range(3)]
for _ in range(M1):
    a,b = map(int,input().split())
    graph[0][a].append(b)
    graph[0][b].append(a)
for _ in range(M2):
    a,b = map(int,input().split())
    graph[1][a].append(b)
    graph[1][b].append(a)
for _ in range(M3):
    a,b = map(int,input().split())
    graph[2][a].append(b)
    graph[2][b].append(a)

arr = [[0]*3 for _ in range(N+1)]
for i in range(3):
    visited = [False]*(N+1)
    for j in range(1,N+1):
        if not visited[j]:
            visited[j] = True
            arr[j][i] = j
            q = [j]
            while q:
                x = q.pop()
                for nx in graph[i][x]:
                    if not visited[nx]:
                        visited[nx] = True
                        arr[nx][i] = j
                        q.append(nx)

study = defaultdict(list)
for i in range(N+1):
    study[tuple(arr[i])].append(i)

result = []
for k in study:
    if len(study[k]) > 1:
        result.append(sorted(study[k]))
print(len(result))
for r in sorted(result):
    print(*r)