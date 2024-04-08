# 골목 대장 호석 - 기능성
# Gold 5, backtracking

def dfs(x,y,z):
    global result
    if y > c: return
    if x == b:
        result = min(result,z)
        return
    for nx,nd in graph[x]:
        if not visited[nx]:
            visited[nx] = True
            dfs(nx,y+nd,max(z,nd))
            visited[nx] = False

n,m,a,b,c = map(int,input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    d,e,f = map(int,input().split())
    graph[d].append((e,f))
    graph[e].append((d,f))

result = 99999
visited = [False]*(n+1)
visited[a] = True
dfs(a,0,0)
print(result if result != 99999 else -1)