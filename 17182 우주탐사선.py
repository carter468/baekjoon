# 우주 탐사선
# Gold 3, floyd-warshall, backtracking

def bt(node,count,cost):
    global result
    
    if count == n:
        result = min(result,cost)
        return
    
    for i in range(n):
        if not visit[i]:
            visit[i] = 1
            bt(i,count+1,cost+graph[node][i])
            visit[i] = 0
    
n,m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]

for k in range(n):
    for i in range(n):
        for j in range(n):
            graph[i][j] = min(graph[i][j],graph[i][k]+graph[k][j])

visit = [0]*n
visit[m] = 1
result = 10**9
bt(m,1,0)
print(result)