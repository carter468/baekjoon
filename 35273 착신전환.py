# 착신 전환
# Gold 2, DFS

def dfs(s):
    q = [s]
    while q:
        x = q.pop()
        for nx in graph[x]:
            if result[nx] == 0:
                result[nx] = result[s]
                q.append(nx)

N = int(input())
A = [0]+list(map(int,input().split()))

graph = [[] for _ in range(N+1)]
for i in range(1,N+1):
    graph[A[i]].append(i)

result = [0]*(N+1)
visited = [False]*(N+1)
for i in range(1,N+1):
    if result[i] == 0:
        while True:
            visited[i] = True
            j = A[i]
            if result[j]:
                break
            if visited[j]:
                arr = [j]
                result[j] = i
                t = j
                while A[j] != t:
                    result[A[j]] = j
                    j = A[j]
                    arr.append(j)
                for s in arr:
                    dfs(s)
                break
            i = j

print(*result[1:])