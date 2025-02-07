# 연료가 부족해
# Gold 2, binary search, priority queue

import sys,heapq
input = sys.stdin.readline

def check(k):
    q = [(-k,0)]
    val = [1]*N
    while q:
        d,x = heapq.heappop(q)
        if R-arr[x][0]+C-arr[x][1] <= -d: return True
        if val[x] <= d: continue
        val[x] = d
        for nx,dd,f in graph[x]:
            if d+dd <= 0:
                heapq.heappush(q,(d+dd-f,nx))
    return False

R,C = map(int,input().split())
N = int(input())+1
arr = [(1,1,0)]+[tuple(map(int,input().split())) for _ in range(N-1)]

graph = [[] for _ in range(N)]
for i in range(N):
    r1,c1,f1 = arr[i]
    for j in range(i+1,N):
        r2,c2,f2 = arr[j]
        if r1 <= r2 and c1 <= c2:
            graph[i].append((j,r2-r1+c2-c1,f2))
        elif r2 <= r1 and c2 <= c1:
            graph[j].append((i,r1-r2+c1-c2,f1))
            
lo,hi = 0,1<<20
while lo+1 < hi:
    mid = (lo+hi)//2
    if check(mid): hi = mid
    else: lo = mid
print(hi)