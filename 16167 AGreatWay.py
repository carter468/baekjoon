# A Great Way
# Gold 3, dijkstra, floyd-warshall

# dijkstra 64ms
import sys,heapq
input = sys.stdin.readline

n,r = map(int,input().split())
graph = [[] for _ in range(n+1)]
for _ in range(r):
    a,b,c,d,e = map(int,input().split())
    graph[a].append((b,c+max(0,e-10)*d))

dist = [[10**5,0] for _ in range(n+1)]
dist[1] = [0,1]
q = [(0,1)]
while q:
    di,lo = heapq.heappop(q)
    if di < dist[lo][0]: continue
    for l,d in graph[lo]:
        d += di
        if d < dist[l][0]:
            dist[l] = [d,dist[lo][1]+1]
            heapq.heappush(q,(d,l))
        elif d == dist[l][0]:
            dist[l][1] = min(dist[l][1],dist[lo][1]+1)

if dist[n][0] == 10**5: print('It is not a great way.')
else: print(*dist[n])

# floyd-warshall 384ms
# import sys
# input = sys.stdin.readline

# n,r = map(int,input().split())
# dist = [[[10**5,0] for _ in range(n+1)] for _ in range(n+1)]
# for _ in range(r):
#     a,b,c,d,e = map(int,input().split())
#     dist[a][b] = [min(dist[a][b][0],c+max(0,e-10)*d),1]

# for k in range(1,n+1):
#     for i in range(1,n+1):
#         for j in range(1,n+1):
#             if dist[i][j][0] > dist[i][k][0]+dist[k][j][0]:
#                 dist[i][j] = [dist[i][k][0]+dist[k][j][0],dist[i][k][1]+dist[k][j][1]]
#             elif dist[i][j][0] == dist[i][k][0]+dist[k][j][0]:
#                 dist[i][j][1] = min(dist[i][j][1],dist[i][k][1]+dist[k][j][1])

# if dist[1][n][0] == 10**5: print('It is not a great way.')
# else: print(dist[1][n][0],dist[1][n][1]+1)