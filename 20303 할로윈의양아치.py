# 할로윈의 양아치
# Gold 3, knapsack, disjoint set

import sys
input = sys.stdin.readline

n,m,k = map(int,input().split())
arr = list(map(int,input().split()))

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

parent = list(range(n))
count = [1]*n
for _ in range(m):
    a,b = map(int,input().split())
    a,b = find(a-1),find(b-1)
    if a != b:
        parent[a] = b
        arr[b] += arr[a]
        count[b] += count[a]

dp = [0]*k
for i in range(n):
    if find(i) == i:
        candy,kid = arr[i],count[i]
        for j in range(k-1,kid-1,-1):
            dp[j] = max(dp[j],dp[j-kid]+candy)

print(dp[-1])