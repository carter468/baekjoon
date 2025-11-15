# 트리 펴기
# Gold 4, ad hoc

import sys
input = sys.stdin.readline

N = int(input())
degree = [0]*(N+1)
for _ in range(N-1):
    u,v = map(int,input().split())
    degree[u] += 1
    degree[v] += 1

result = 0
for i in range(N+1):
    result += max(0,degree[i]-2)
print(result)