# 돌멩이제거

import sys
input = sys.stdin.readline

n,k = map(int,input().split())
stone = [[] for _ in range(n+1)]
matching = [0]*(n+1)
for i in range(k):
    a,b = map(int,input().split())
    stone[a].append(b)

def dfs(idx):
    if visit[idx]:
        return 0
    visit[idx] = 1
    for i in stone[idx]:
        if matching[i] == 0 or dfs(matching[i]):
            matching[i] = idx
            return 1
    return 0
    
for i in range(1,n+1):
    visit = [0]*(n+1)
    dfs(i)
print(n+1-matching.count(0))