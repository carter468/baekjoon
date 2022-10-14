# 열혈강호

import sys
input = sys.stdin.readline

n,m = map(int,input().split())
graph = [[]]
for i in range(n):
    task = list(map(int,input().split()))
    graph.append(task[1:])
matching = [0 for _ in range(m+1)]

def dfs(node):
    if visit[node]:
        return False
    visit[node] = 1
    for next in graph[node]:
        if matching[next] == 0:
            matching[next] = node
            return True
        else:
            prev = matching[next]
            if dfs(prev):
                matching[next] = node
                return True
    return False

for i in range(1,n+1):
    visit = [0 for _ in range(n+1)]
    dfs(i)
ans = 0
for i in range(m+1):
    if matching[i]>0:
        ans += 1
print(matching)
print(ans)
print(m-matching.count(0)+1)
