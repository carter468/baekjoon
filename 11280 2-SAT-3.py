# 2-SAT - 3

import sys
sys.setrecursionlimit(10**6)

n,m = map(int,input().split())
graph = [[] for _ in range(2*n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    graph[-a].append(b)
    graph[-b].append(a)

scc_num = 1
idx = 1
stack = []
scc_idx = [0]*(2*n+1)
check = [0]*(2*n+1)
visited = [0]*(2*n+1)

def scc(node):
    global idx,scc_num
    visited[node] = idx
    root = idx
    idx += 1
    stack.append(node)

    for now in graph[node]:
        if not visited[now]:
            root = min(root,scc(now))
        elif not check[now]:
            root = min(root,visited[now])
        
    if root == visited[node]:
        while stack:
            top = stack.pop()
            check[top] = 1
            scc_idx[top] = scc_num
            if node == top:
                break
        scc_num += 1
    
    return root

for i in range(1,n+1):
    if not visited[i]:
        scc(i)
for i in range(1,n+1):
    if scc_idx[i] == scc_idx[-i]:
        print(0)
        break
else:
    print(1)