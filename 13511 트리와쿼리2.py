# 트리와 쿼리 2

from collections import deque
import sys,math
input = sys.stdin.readline

n = int(input())
tree = [[] for _ in range(n+1)]
for _ in range(n-1):
    a,b,c = map(int,input().split())
    tree[a].append([b,c])
    tree[b].append([a,c])

parent = [[0,0] for _ in range(n+1)]
depth = [0]*(n+1)
visit = [False]*(n+1)
q = deque([1])
visit[1] = True
while q:
    now = q.popleft()
    for b,c in tree[now]:
        if not visit[b]:
            q.append(b)
            parent[b][0] = now
            parent[b][1] = c
            depth[b] = depth[now] + 1
            visit[b] = True

l = int(math.log2(n)) + 1
dp = [[[0,0] for _ in range(l)] for _ in range(n+1)]
for i in range(n+1):
    dp[i][0][0] = parent[i][0]
    dp[i][0][1] = parent[i][1]
for j in range(1,l):
    for i in range(1,n+1):
        dp[i][j][0] = dp[dp[i][j-1][0]][j-1][0]
        dp[i][j][1] = dp[i][j-1][1] + dp[dp[i][j-1][0]][j-1][1]

m = int(input())
for _ in range(m):
    q = list(map(int,input().split()))
    u,v = q[1],q[2]
    u2,v2 = u,v
    if depth[u] < depth[v]:
        u2,v2 = v2,u2
    diff = depth[u2]-depth[v2]
    for i in range(l):
        if diff & 1<<i:
            u2 = dp[u2][i][0]
    if u2 == v2:
        lca = u2
    else:
        for i in range(l-1,-1,-1):
            if dp[u2][i][0] != dp[v2][i][0]:
                u2 = dp[u2][i][0]
                v2 = dp[v2][i][0]
        lca = dp[u2][0][0]
    if q[0] == 1:
        cost = 0
        diff_u = depth[u] - depth[lca]
        diff_v = depth[v] - depth[lca]
        for i in range(l):
            if diff_u & 1<<i:
                cost += dp[u][i][1]
                u = dp[u][i][0]
            if diff_v & 1<<i:
                cost += dp[v][i][1]
                v = dp[v][i][0]
        print(cost)
    else:
        k = q[3]
        if k <= depth[u]-depth[lca]:
            diff = k-1
            for i in range(l):
                if diff & 1<<i:
                    u = dp[u][i][0]
            print(u)
        else:
            diff = depth[u] + depth[v] - depth[lca]*2 - k+1
            for i in range(l-1,-1,-1):
                if diff & 1<<i:
                    v = dp[v][i][0]
            print(v)
            
# from collections import deque
# import sys,math
# input = sys.stdin.readline

# n = int(input())
# l = int(math.log2(n))+1
# graph = [[] for _ in range(n+1)]
# for _ in range(n-1):
#     u,v,w = map(int,input().split())
#     graph[u].append([v,w])
#     graph[v].append([u,w])

# parent = [[0,0] for _ in range(n+1)]
# depth = [0 for _ in range(n+1)]
# visited = [False for _ in range(n+1)]
# q = deque([1])
# visited[1] = True
# while q:
#     x = q.popleft()
#     for v,c in graph[x]:
#         if visited[v] == False:
#             q.append(v)
#             depth[v] = depth[x] + 1
#             visited[v] = True
#             parent[v][0] = x
#             parent[v][1] = c
# dp = [[[0,0] for _ in range(n+1)] for _ in range(l)]
# for i in range(n+1):
#     dp[0][i][0] = parent[i][0]
#     dp[0][i][1] = parent[i][1]

# for i in range(1,l):
#     for j in range(1,n+1):
#         dp[i][j][0] = dp[i-1][dp[i-1][j][0]][0]
#         dp[i][j][1] = dp[i-1][j][1] + dp[i-1][dp[i-1][j][0]][1]

# def cost(a,b):
#     ans = 0
#     if depth[a] < depth[b]:
#         a,b = b,a
#     diff = depth[a] - depth[b]
#     for i in range(l):
#         if diff & 1<<i:
#             ans += dp[i][a][1]
#             a = dp[i][a][0]
#     if a == b:
#         return ans
#     for i in range(l-1,-1,-1):
#         if dp[i][a][0] != dp[i][b][0]:
#             ans += dp[i][a][1]+dp[i][b][1]
#             a = dp[i][a][0]
#             b = dp[i][b][0]
#     return ans

# def findk(u,v,k):
#     a,b = u,v
#     lca = 0
#     if depth[a] < depth[b]:
#         a,b = b,a
#     diff = depth[a] - depth[b]
    
#     for i in range(l):
#         if diff & 1<<i:
#             a = dp[i][a][0]
#     if a == b:
#         lca = a
#     else:
#         for i in range(l-1,-1,-1):
#             if dp[i][a][0] != dp[i][b][0]:
#                 a = dp[i][a][0]
#                 b = dp[i][b][0]
#         lca = a
#     if k <= depth[u] - depth[lca]:
#         k -= 1
#         for i in range(l):
#             if k & 1<<i:
#                 u = dp[i][u][0]
#         return u
#     else:
#         k = depth[u]-depth[lca] + depth[v]-depth[lca] - k+1
#         for i in range(l):
#             if k & 1<<i:
#                 v = dp[i][v][0]
#         return v

# m = int(input())
# for _ in range(m):
#     q = list(map(int,input().split()))
#     if q[0] == 1:
#         u,v = q[1:]
#         print(cost(u,v))
#     else:
#         u,v,k = q[1:]
#         print(findk(u,v,k))