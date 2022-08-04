# 플로이드2

import sys
input = sys.stdin.readline

n = int(input())    # 도시의 개수
m = int(input())    # 버스의 개수

graph = [[]*(n+1) for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append([b,c])

print(graph)