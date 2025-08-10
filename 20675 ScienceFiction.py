# Science Fiction
# Gold 2, BFS, constructive

from collections import deque,defaultdict

N = int(input())
A = list(map(int,input().split()))

graph = defaultdict(list)
for i in range(1<<N):
    for j in range(i+1,1<<N):
        diff = i^j
        if diff&(diff-1) == 0:
            graph[i].append(j)
            graph[j].append(i)

pos = {}
for i,a in enumerate(A):
    pos[a] = i
B = sorted(A)

result = []
for i in range(1<<N):
    s = pos[B[i]]
    visited = [-1]*(1<<N)
    visited[s] = 0
    q = deque([s])
    while q:
        x = q.popleft()
        if x == i: break
        for nx in graph[x]:
            if visited[nx] == -1 and nx >= i:
                visited[nx] = visited[x]+1
                q.append(nx)
    
    temp = [i]
    while x != s:
        for nx in graph[x]:
            if visited[nx] == visited[x]-1:
                temp.append(nx)
                x = nx
                break

    x = temp.pop()
    while temp:
        nx = temp.pop()
        a,b = A[x],A[nx]
        A[nx],A[x] = a,b
        pos[a],pos[b] = nx,x
        result.append((x,nx))
        x = nx

print(len(result))
for r in result: print(*r)