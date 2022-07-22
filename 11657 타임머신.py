# 타임머신

import sys
input = sys.stdin.readline

n,m = map(int,input().split())  # 도시의 개수,버스 노선의 개수

INF = int(10**9)
edges = []                      # 노선 정보
distance = [INF]*(n+1)          # 최단거리테이블

for _ in range(m):
    edges.append(list(map(int,input().split())))

# Bellman-Ford 알고리즘
def bellmanford():
    distance[1] = 0

    for i in range(n):  # n-1번 반복, 마지막 1번은 음수순환 확인
        for j in range(m):
            curr_node = edges[j][0]
            next_node = edges[j][1]
            cost = edges[j][2]
            if distance[curr_node] != INF and distance[next_node] > distance[curr_node] + cost:
                distance[next_node] = distance[curr_node] + cost
                if i == n-1:    # 음수순환 확인
                    return True
    return False

if bellmanford():
    print(-1)
else:
    for i in range(2,n+1):
        if distance[i] == INF:
            print(-1)
        else:
            print(distance[i])