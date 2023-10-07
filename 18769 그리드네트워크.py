# 그리드 네트워크
# Gold 4, MST

# Prim algorithm : TLE

# import sys,heapq
# input = sys.stdin.readline

# for _ in range(int(input())):
#     r,c = map(int,input().split())
#     cost_r = [tuple(map(int,input().split())) for _ in range(r)]
#     cost_c = [tuple(map(int,input().split())) for _ in range(r-1)]

#     visit = [[0]*c for _ in range(r)]
#     q = [(0,0,0)]
#     result = 0
#     while q:
#         d,x,y = heapq.heappop(q)
#         if not visit[x][y]:
#             visit[x][y] = 1
#             result += d
#             if x+1 < r and not visit[x+1][y]:
#                 heapq.heappush(q,(cost_c[x][y],x+1,y))
#             if x-1 >= 0 and not visit[x-1][y]:
#                 heapq.heappush(q,(cost_c[x-1][y],x-1,y))
#             if y+1 < c and not visit[x][y+1]:
#                 heapq.heappush(q,(cost_r[x][y],x,y+1))
#             if y-1 >= 0 and not visit[x][y-1]:
#                 heapq.heappush(q,(cost_r[x][y-1],x,y-1))
#     print(result)

# Kruskal algorithm : AC

import sys
input = sys.stdin.readline

def find(x):
    if root[x] != x:
        root[x] = find(root[x])
    return root[x]

for _ in range(int(input())):
    r,c = map(int,input().split())
    edge = []
    root = list(range(r*c+1))

    node = 1
    for i in range(r):
        for d in map(int,input().split()):
            edge.append((d,node,node+1))
            node += 1
        node += 1
    
    node = 1
    for i in range(r-1):
        for d in map(int,input().split()):
            edge.append((d,node,node+c))
            node += 1

    edge.sort()
    result = 0
    for d,x,y in edge:
        x,y = find(x),find(y)
        if x != y:
            if x > y: root[x] = y
            else: root[y] = x
            result += d
    print(result)