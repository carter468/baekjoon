# Bad Horse (Small1)
# Gold 4, DFS, bipartite graph, hash_set

from collections import defaultdict

def dfs(x):
    global result
    for nx in graph[x]:
        if nx in visited:
            if visited[nx] == visited[x]:
                result = 'No'
                return
        else:
            visited[nx] = -visited[x]
            dfs(nx)          
        
for i in range(int(input())):
    graph = defaultdict(set)
    for _ in range(int(input())):
        a,b = input().split()
        graph[a].add(b)
        graph[b].add(a)
    
    result = 'Yes'
    visited = {}
    for x in graph:
        if x not in visited:
            visited[x] = 1
            dfs(x)
    print(f'Case #{i+1}: {result}')