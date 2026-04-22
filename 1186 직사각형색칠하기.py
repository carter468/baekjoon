# 직사각형 색칠하기
# Gold 3, greedy, coordinate compression

N,K = map(int,input().split())
arr = [tuple(map(int,input().split())) for _ in range(N)]

x,y = set(),set()
for x1,y1,x2,y2 in arr:
    x.update((x1,x2))
    y.update((y1,y2))

x = sorted(x)
y = sorted(y)
dic_x = dict()
dic_y = dict()
lx = len(x)
ly = len(y)
for i in range(lx):
    dic_x[x[i]] = i
for i in range(ly):
    dic_y[y[i]] = i

grid = [[0]*ly for _ in range(lx)]
for n in range(N):
    x1,y1,x2,y2 = arr[n]
    x1,y1,x2,y2 = dic_x[x1],dic_y[y1],dic_x[x2],dic_y[y2]
    for i in range(x1,x2):
        for j in range(y1,y2):
            grid[i][j] = n+1

area = [0]*(N+1)
for i in range(lx-1):
    for j in range(ly-1):
        area[grid[i][j]] += (x[i+1]-x[i])*(y[j+1]-y[j])

print(*sorted([i for i,_ in sorted([(i,area[i]) for i in range(1,N+1)],key=lambda x:(-x[1],x[0]))[:K]]))