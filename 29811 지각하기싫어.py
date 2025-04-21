# 지각하기 싫어
# Gold 4, priority queue

import sys,heapq
input = sys.stdin.readline

N,M = map(int,input().split())
arr = tuple(map(int,input().split()))
arr1 = [0]*(N+1)
q1 = []
for i in range(N):
    arr1[i+1] = arr[i]
    heapq.heappush(q1,(arr[i],i+1))
arr = tuple(map(int,input().split()))
arr2 = [0]*(M+1)
q2 = []
for i in range(M):
    arr2[i+1] = arr[i]
    heapq.heappush(q2,(arr[i],i+1))

for _ in range(int(input())):
    query = input().split()
    if query[0] == 'U':
        x,y = map(int,query[1:])
        if x <= N:
            arr1[x] = y
            heapq.heappush(q1,(y,x))
        else:
            arr2[x-N] = y
            heapq.heappush(q2,(y,x-N))
    elif query[0] == 'L':
        while q1:
            y,x = q1[0]
            if arr1[x] == y: break
            heapq.heappop(q1)
        while q2:
            y,x = q2[0]
            if arr2[x] == y: break
            heapq.heappop(q2)
        print(q1[0][1],q2[0][1]+N)