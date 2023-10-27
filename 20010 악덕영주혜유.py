# 악덕 영주 혜유
# Gold 2, MST, diameter of a tree

from collections import deque
import sys
input = sys.stdin.readline

n,k = map(int,input().split())
edge = []
for _ in range(k):
    a,b,c = map(int,input().split())
    edge.append((c,a,b))

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

graph = [[] for _ in range(n)]
parent = list(range(n))
total_cost = 0
for c,x,y in sorted(edge):
    a,b = find(x),find(y)
    if a != b:
        graph[x].append((y,c))
        graph[y].append((x,c))
        if a > b: parent[a] = b
        else: parent[b] = a
        total_cost += c
print(total_cost)

def bfs(start):
    q = deque([(start,0)])
    visit = [False]*n
    visit[start] = True
    max_node = 0
    max_cost = 0
    while q:
        node,cost = q.popleft()
        if cost > max_cost:
            max_cost = cost
            max_node = node
        for next_node,next_cost in graph[node]:
            if visit[next_node] == False:
                visit[next_node] = True
                q.append((next_node,cost+next_cost))
    return max_node,max_cost

print(bfs(bfs(0)[0])[1])