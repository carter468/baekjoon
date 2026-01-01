# Soju
# Platinum 4, priority queue

import sys,heapq
input = sys.stdin.readline

for _ in range(int(input())):
    N = int(input())
    I = sorted([tuple(map(int,input().split())) for _ in range(N)],key=lambda x:x[1])
    M = int(input())
    P = sorted([tuple(map(int,input().split())) for _ in range(M)],key=lambda x:x[1])

    result = 10**9
    heap1 = []
    heap2 = []
    j,k = 0,M-1
    for i in range(N):
        x1,y1 = I[i]
        while j < M and y1 >= P[j][1]:
            x2,y2 = P[j]
            heapq.heappush(heap1,(x2-y2,x2,y2))
            j += 1
        if heap1:
            _,x2,y2 = heap1[0]
            result = min(result,x2-x1+y1-y2)

        x1,y1 = I[-1-i]
        while k >= 0 and y1 <= P[k][1]:
            x2,y2 = P[k]
            heapq.heappush(heap2,(x2+y2,x2,y2))
            k -= 1
        if heap2:
            _,x2,y2 = heap2[0]
            result = min(result,x2-x1+y2-y1)
    
    print(result)