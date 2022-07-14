# 이분그래프

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(x,z):
    visited[x] = z                        

    for i in graph[x]:
        if visited[i] == 0:
            if not dfs(i,-z):  
                return False         
        if visited[i] == visited[x]:    # 인접한 색이 같으면 이분그래프아님
            return False
    return True

k = int(input())
for _ in range(k):
    v,e = map(int,input().split())
    graph = [[] for _ in range(v+1)]
    for _ in range(e):
        a,b = map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)

    visited = [0] * (v+1)   # 색칠할 곳 - 0:방문안함 1:빨강 -1:파랑 
    d = True                # 이분그래프 판별

    for i in range(1,v+1):    # 모든 방문하지않은 정점 탐색
        if visited[i] == 0:
            d = dfs(i,1)
            if d == False:
                print('NO')
                break

    if d == True:
        print('YES')