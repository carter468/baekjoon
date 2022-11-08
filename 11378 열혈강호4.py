# 열혈강호 4

import sys
input = sys.stdin.readline

n,m,k = map(int,input().split())
graph = [[] for _ in range(n+1)]
matching = [0 for _ in range(m+1)]
count = 0

for i in range(1,n+1):
    a = list(map(int,input().split()))
    for j in a[1:]:
        graph[i].append(j)

def dfs(start):
    if visit[start]:
        return 0
    visit[start] = 1
    for i in graph[start]:
        if not matching[i] or dfs(matching[i]):
            matching[i] = start
            return 1
    return 0
    
for i in range(1,n+1):
    visit = [0 for _ in range(n+1)]
    count += dfs(i)
for i in range(1,n+1):
    while k>0:
        visit = [0 for _ in range(n+1)]
        if dfs(i):
            k -= 1
            count += 1
        else:
            break
print(count)