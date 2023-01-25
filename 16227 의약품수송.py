# 의약품 수송
# Gold 1, 데이크스트라

import heapq
import sys
input = sys.stdin.readline
INF = sys.maxsize

def dijkstra():
    distance = [INF]*(N+2)
    distance[0] = 0
    q = []
    heapq.heappush(q,(0,0,0))   # 시간,위치,모래
    while q:
        d,l,s = heapq.heappop(q)
        for nd,nl in graph[l]:
            ts = s+nd   # 모래의 양
            if nl==N+1: # 도착지점
                if ts>100:  
                    td = d+nd+5 
                else:       
                    td = d+nd
            else:
                if nd==100:
                    if s==0:
                        td = d+nd+5
                    else:
                        td = d+nd+10
                    ts = 0
                elif ts>100:
                    td = d+nd+5
                    ts = nd
                else:
                    td = d+nd

            if td<distance[nl]:
                distance[nl] = td
                heapq.heappush(q,(td,nl,ts))
    
    return distance[N+1]

N,K = map(int,input().split())  # 특수장비수, 도로수
graph = [[] for _ in range(N+2)]
for _ in range(K):
    u,v,t = map(int,input().split())
    if t>100:
        continue
    graph[u].append((t,v))
    graph[v].append((t,u))

print(dijkstra())