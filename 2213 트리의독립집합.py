# 트리의 독립집합

def dfs(start):
    visited[start] = 1
    dp[start][0] = weight[start]
    mis[start][0].append(start)
    
    for i in graph[start]:
        if not visited[i]:
            dfs(i)
            dp[start][0] += dp[i][1]
            for j in mis[i][1]:
                mis[start][0].append(j)
            if dp[i][0] <= dp[i][1]:
                dp[start][1] += dp[i][1]
                for j in mis[i][1]:
                    mis[start][1].append(j)
            else:
                dp[start][1] += dp[i][0]
                for j in mis[i][0]:
                    mis[start][1].append(j)

n = int(input())
weight = [0] + list(map(int,input().split()))
graph = [[] for _ in range(n+1)]  
for _ in range(n-1):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0]*(n+1)
dp = [[0,0] for _ in range(n+1)]
mis = [[[],[]] for _ in range(n+1)]

dfs(1)
if dp[1][0] >= dp[1][1]:
    idx = 0
else:
    idx = 1
ans = mis[1][idx]
ans.sort()
print(dp[1][idx])
print(*ans)