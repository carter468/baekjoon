# ATM

import sys
from collections import deque
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(node):
    visit[node] = 1
    for now in graph[node]:
        if not visit[now]:
            dfs(now)
    stack.append(node)

def reverse_dfs(node,num):
    scc_num[node] = num
    scc_arr[num] += 1
    scc_val[num] += cash[node]
    for now in reverse_graph[node]:
        if scc_num[now] == -1:
            reverse_dfs(now,num)
        elif scc_num[node] != scc_num[now]:
            group[scc_num[now]].append(scc_num[node])
    
n,m = map(int,input().split())
graph = [[] for _ in range(n)]
reverse_graph = [[] for _ in range(n)]
visit = [0]*n
stack = []
scc_num = [-1]*n
scc_arr = []
group = []

for i in range(m):
    a,b = map(int,input().split())
    graph[a-1].append(b-1)
    reverse_graph[b-1].append(a-1)

cash = [int(input()) for _ in range(n)]

for i in range(n):
    if not visit[i]:
        dfs(i)

scc_val = []
k = 0
while stack:
    now = stack.pop()
    if scc_num[now] == -1:
        group.append([])
        scc_arr.append(0)
        scc_val.append(0)
        reverse_dfs(now,k)
        k += 1

s,p = map(int,input().split())
s += -1
result = list(map(int,input().split()))

q = deque([scc_num[s]])
dp = [0]*k
dp[scc_num[s]] = scc_val[scc_num[s]]
while q:
    now = q.popleft()
    for n in group[now]:
        if dp[n] < dp[now]+scc_val[n]:
            dp[n] = dp[now]+scc_val[n]
            q.append(n)

ans = 0
for x in result:
    ans = max(ans,dp[scc_num[x-1]])
print(ans)