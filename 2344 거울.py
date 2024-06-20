# 거울
# Gold 4, implementation, simulation

D = [(0,1),(-1,0),(0,-1),(1,0)]

n,m = map(int,input().split())
arr = [tuple(map(int,input().split())) for _ in range(n)]

hole = {}
idx = 1
for i in range(n):
    hole[(i,-1)] = (idx,0)
    idx += 1
for i in range(m):
    hole[(n,i)] = (idx,1)
    idx += 1
for i in range(n):
    hole[(n-i-1,m)] = (idx,2)
    idx += 1
for i in range(m):
    hole[(-1,m-i-1)] = (idx,3)
    idx += 1

result = [0]*((n+m)*2+1)
for x,y in hole:
    s,d = hole[(x,y)]
    if result[s] == 0:
        x += D[d][0]
        y += D[d][1]
        while (x,y) not in hole:
            if arr[x][y] == 1:
                if d <= 1: d = 1-d
                else: d = 5-d
            x += D[d][0]
            y += D[d][1]
        e = hole[(x,y)][0]
        result[s] = e
        result[e] = s

print(*result[1:])