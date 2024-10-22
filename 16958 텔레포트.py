# 텔레포트
# Gold 4, bruteforcing

import sys
input = sys.stdin.readline

n,t = map(int,input().split())
arr = [tuple(map(int,input().split())) for _ in range(n)]
adj = [9999]*n

# 텔포는 0번 타거나 1번 타는 방법 중에 최소이동시간이 있다.
# 각 정점에서 텔포를 탈 수 있는 정점까지 가장 가까운 거리를 저장해놓으면(adj배열)
# 두 점 사이의 최소이동시간은 
# min(두점사이의거리(텔포0번),두 정점에서 텔포를 탈 수 있는 곳으로 이동시간+T(텔포1번))
# 시간복잡도는 O(n^2)

for i in range(n):
    if arr[i][0] == 1:
        adj[i] = 0
        continue
    for j in range(n):
        if arr[j][0] == 1:
            adj[i] = min(adj[i],abs(arr[i][1]-arr[j][1])+abs(arr[i][2]-arr[j][2]))

for _ in range(int(input())):
    a,b = map(int,input().split())
    a,b = a-1,b-1
    print(min(abs(arr[a][1]-arr[b][1])+abs(arr[a][2]-arr[b][2]),adj[a]+adj[b]+t))