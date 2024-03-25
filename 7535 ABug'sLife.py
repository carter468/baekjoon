# A Bug's Life
# Gold 3, DFS

import sys
sys.setrecursionlimit(9999)
input = sys.stdin.readline

def dfs(x):
    global flag
    for nx in graph[x]:
        if gender[nx] == gender[x]: flag = True
        elif gender[nx] == 0:
            gender[nx] = 3-gender[x]
            dfs(nx)
        
for idx in range(int(input())):
    n,m = map(int,input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a,b = map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)

    print(f'Scenario #{idx+1}:')
    gender = [0]*(n+1)
    for i in range(1,n+1):
        if gender[i] == 0 and graph[i]:
            flag = False
            gender[i] = 1
            dfs(i)
            if flag:
                print('Suspicious bugs found!')
                break
    else: print('No suspicious bugs found!')
    print()