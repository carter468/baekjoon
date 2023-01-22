# 환승
# Gold 2, 너비 우선 탐색

from collections import deque
import sys
input = sys.stdin.readline

N,K,M = map(int,input().split())    # 역 개수, 튜브크기, 튜브개수

station = [[] for _ in range(N+1)]  
visit = [0]*(N+M+1)

for i in range(M):
    station.append(tuple(map(int,input().split())))
    for j in station[-1]:
        station[j].append(N+i+1)

q = deque([1])
visit[1] = 1
while q:
    now = q.popleft()
    if now==N:
        print(visit[now])
        break
    for i in station[now]:
        if visit[i]==0:
            if i>N:
                visit[i] = visit[now]
            else:
                visit[i] = visit[now]+1
            q.append(i)
else:
    print(-1)