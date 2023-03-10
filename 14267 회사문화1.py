# 회사 문화 1
# Gold 4, dp

import sys
input = sys.stdin.readline

n,m = map(int,input().split())
boss = [0]*(n+1)
for i,b in enumerate(map(int,input().split())):
    boss[i+1] = b
result = [0]*(n+1)
for _ in range(m):
    i,w = map(int,input().split())
    result[i] += w

for i in range(2,n+1):
    result[i] += result[boss[i]]

print(*result[1:])