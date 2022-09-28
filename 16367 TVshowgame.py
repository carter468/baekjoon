# TV Show Game

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

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
            scc_arr[top] = scc_num
            if node == top:
                break
        scc_num += 1
    return root

def neg(a):
    if a<=k:return a+k
    else: return a-k

k,n = map(int,input().split())
graph = [[] for _ in range(k*2+1)]
for _ in range(n):
    a1,a2,b1,b2,c1,c2 = list(input().rstrip().split())
    a1,b1,c1 = map(int,[a1,b1,c1])
    if a2 == 'B':
        a1+=k
    if b2 == 'B':
        b1+=k
    if c2 == 'B':
        c1+=k
    graph[neg(a1)].append(b1)
    graph[neg(a1)].append(c1)
    graph[neg(b1)].append(a1)
    graph[neg(b1)].append(c1)
    graph[neg(c1)].append(a1)
    graph[neg(c1)].append(b1)

idx = scc_num = 0
check = [False for _ in range(k*2+1)]
scc_arr = [0 for _ in range(k*2+1)]
visited = [0 for _ in range(k*2+1)]
stack = []
for i in range(1,k*2+1):
    if check[i]:
        continue
    scc(i)
for i in range(1,k+1):
    if scc_arr[i] == scc_arr[i+k]:
        print(-1)
        exit(0)
for i in range(1,k+1):
    if scc_arr[i] > scc_arr[i+k]:
        print('B',end='')
    else:
        print('R',end='')