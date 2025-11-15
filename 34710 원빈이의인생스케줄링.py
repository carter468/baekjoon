# 원빈이의 인생 스케줄링
# Gold 3, greedy, prioirty queue

import sys,heapq
input = sys.stdin.readline
M = 200001

arr = sorted([tuple(map(int,input().split())) for _ in range(int(input()))])

heap = []
k = 0
i = 1
check = [False]*M
job = [0]*M
for t,l in arr:
    job[t] += 1
    for j in range(i,t+1):
        heapq.heappush(heap,-j)
    while k < l:
        if not heap: exit(print(-1))
        idx = heapq.heappop(heap)
        check[-idx] = True
        k += 1
    i = t+1

k = s = 0
result = 0
for i in range(1,M):
    if check[i]: k += 1
    else: s += 1
    result += job[i]*s
print(result)