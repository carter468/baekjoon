# 트리

from collections import deque

def bfs(root):
    visit = [False]*n
    cnt = 0
    q = deque([root])
    while q:
        x = q.popleft()
        if not tree[x]:
            cnt += 1
        for node in tree[x]:
            if not visit[node]:
                q.append(node)
                visit[node] = True
    return cnt

n = int(input())
parent = list(map(int,input().split()))
node_delete = int(input())
tree = [[] for _ in range(n)]
for i in range(n):
    if parent[i] == -1:
        root = i
        continue
    if i == node_delete:
        continue
    tree[parent[i]].append(i)
if root == node_delete:
    print(0)
else:
    print(bfs(root))