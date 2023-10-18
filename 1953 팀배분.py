# 팀 배분
# Gold 4, DFS, bipartite graph

n = int(input())
graph = [[] for _ in range(n+1)]
for i in range(n):
    for j in map(int,input().split()[1:]):
        graph[i+1].append(j)

team = [-1]*(n+1)
result = [[],[]]
for i in range(1,n+1):
    if team[i] == -1:
        team[i] = 0
        result[0].append(i)
        q = [i]
        while q:
            x = q.pop()
            for nx in graph[x]:
                if team[nx] == -1:
                    team[nx] = team[x]^1
                    result[team[nx]].append(nx)
                    q.append(nx)

print(len(result[0]))
print(*sorted(result[0]))
print(len(result[1]))
print(*sorted(result[1]))