# 제설 작업
# Gold 4, priority queue, prefix sum

import sys,heapq
input = sys.stdin.readline

N,M = map(int,input().split())
A = [tuple(map(int,input().split())) for _ in range(N)]

heap = []
psum = [[0]*M for _ in range(N)]
psumrow = []
for i in range(N):
    for j in range(M):
        psum[i][j] += psum[i-1][j]+A[i][j]
    s = sum(A[i])
    psumrow.append(s)
    heapq.heappush(heap,(s,0,i))
for j in range(M):
    heapq.heappush(heap,(psum[-1][j],1,j))
psumcol = psum[-1]

m = 0
count = N*M
vrow = [True]*N
vcol = [True]*M
while count:
    a,b,idx = heapq.heappop(heap)
    m = max(m,a)
    if b == 0 and vrow[idx]:
        c = 0
        for j in range(M):
            if vcol[j]:
                c += 1
                psumcol[j] -= A[idx][j]
                if psumcol[j] > 0: heapq.heappush(heap,(psumcol[j],1,j))
                vrow[idx] = False
        count -= c
    if b == 1 and vcol[idx]:
        c = 0
        for i in range(N):
            if vrow[i]:
                c += 1
                psumrow[i] -= A[i][idx]
                if psumrow[i] > 0: heapq.heappush(heap,(psumrow[i],0,i))
                vcol[idx] = False
        count -= c

print(m)