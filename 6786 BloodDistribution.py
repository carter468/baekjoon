# Blood Distribution
# Platinum 4, flow

# dinic

from collections import deque
INF = 10**9
MAX = 18
S,T = 16,17

def dinic():
    flow = 0
    while bfs():
        for i in range(MAX):
            work[i] = 0
        while True:
            pushed = dfs(S,INF)
            if pushed == 0:
                break
            flow += pushed
    return flow

def bfs():
    global level
    q = deque([S])
    level = [-1]*MAX
    level[S] = 0
    while q:
        x = q.popleft()
        for to,cap,_ in graph[x]:
            if cap > 0 and level[to] == -1:
                level[to] = level[x]+1
                q.append(to)
    return level[T] != -1

def dfs(x,f):
    if x == T:
        return f
    for i in range(work[x],len(graph[x])):
        work[x] = i
        to,cap,rev = graph[x][i]
        if cap > 0 and level[to] == level[x] + 1:
            pushed = dfs(to,min(f,cap))
            if pushed > 0:
                graph[x][i][1] -= pushed
                graph[to][rev][1] += pushed
                return pushed
    return 0

def add_edge(u,v,cap):
    graph[u].append([v,cap,len(graph[v])])
    graph[v].append([u,0,len(graph[u])-1])

supply = tuple(map(int,input().split()))
demand = tuple(map(int,input().split()))

edge = [[0,1,2,3,4,5,6,7],[1,3,5,7],[2,3,6,7],[3,7],[4,5,6,7],[5,7],[6,7],[7]]
graph = [[] for _ in range(MAX)]
for i in range(8):
    add_edge(S,i,supply[i])

    for j in edge[i]:
        add_edge(i,j+8,INF)

    add_edge(i+8,T,demand[i])

work = [0]*MAX
print(dinic())

# edmond-karf

from collections import deque
INF = 10**9
MAX = 18
S,T = 16,17

supply = tuple(map(int,input().split()))
demand = tuple(map(int,input().split()))

graph = [[] for _ in range(MAX)]
capacity = [[0 for _ in range(MAX)] for _ in range(MAX)]
flow = [[0 for _ in range(MAX)] for _ in range(MAX)]

edge = [[0,1,2,3,4,5,6,7],[1,3,5,7],[2,3,6,7],[3,7],[4,5,6,7],[5,7],[6,7],[7]]
for i in range(8):
    graph[S].append(i)
    graph[i].append(S)
    capacity[S][i] = supply[i]

    for j in edge[i]:
        graph[i].append(j+8)
        graph[j+8].append(i)
        capacity[i][j+8] = INF

    graph[i+8].append(T)
    graph[T].append(i+8)
    capacity[i+8][T] = demand[i]

result = 0
while True:
    path = [-1]*(MAX)
    q = deque([S])
    while q:
        x = q.popleft()
        for nx in graph[x]:
            if  capacity[x][nx]-flow[x][nx] > 0 and path[nx] == -1:
                path[nx] = x
                if nx == T:
                    break
                q.append(nx)
    if path[T] == -1:
        break

    f = INF
    x = T
    while x != S:
        nx = path[x]
        f = min(f,capacity[nx][x]-flow[nx][x])
        x = nx

    x = T
    while x != S:
        nx = path[x]
        flow[nx][x] += f
        flow[x][nx] -= f
        x = nx
    result += f

print(result)