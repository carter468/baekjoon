# Yes or yes
# Gold 4, DFS

import sys
input = sys.stdin.readline

n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    u,v = map(int,input().split())
    graph[u].append(v)
input()
check = [0]*(n+1)
for s in input().split():
    check[int(s)] = -1

if check[1]: print('Yes')
else:
    check[1] = 1
    q = [1]
    while q:
        x = q.pop()
        flag = False
        for nx in graph[x]:
            if check[nx] == 0:
                flag = True
                check[nx] = 1
                q.append(nx)
            elif check[nx] == -1:
                flag = True
        if not flag:
            print('yes')
            break
    else: print('Yes')