# 계보 복원가 호석
# Gold 3, topological sorting, hash set

import sys
input = sys.stdin.readline

input()

indegree = {}
graph = {}
result = {}
names = sorted(input().split())

for name in names:
    indegree[name] = 0
    graph[name] = []
    result[name] = []

for _ in range(int(input())):
    a,b = input().split()
    indegree[a] += 1
    graph[b].append(a)

root = []
q = []
for name in names:
    if indegree[name] == 0:
        q.append(name)
        root.append(name)
while q:
    name = q.pop()
    for child in graph[name]:
        indegree[child] -= 1
        if indegree[child] == 0:
            result[name].append(child)
            q.append(child)

print(len(root))
print(*sorted(root))
for name in names:
    print(name,len(result[name]),*sorted(result[name]),sep=' ')