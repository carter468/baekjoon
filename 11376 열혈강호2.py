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
        if matching[next] == 0:     # 배정된 직원이 없다
            matching[next] = node
            return True
        else:
            prev = matching[next]
            if dfs(prev):           # 이미 배정된 직원이 다른 일에 배정가능한경우
                matching[next] = node
                return True
    return False

for _ in range(2):
    for i in range(1,n+1):
        visit = [0 for _ in range(n+1)]
        dfs(i)
print(m+1-matching.count(0))
