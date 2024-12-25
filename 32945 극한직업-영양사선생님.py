# 극한직업 - 영양사 선생님
# Gold 5, greedy, priority queue

import heapq

N = int(input())
arr = sorted(map(int,input().split()))

answer = 0
q = []
for i in range(N):
    heapq.heappush(q,i+arr.pop())
    while q and q[0] <= i:
        heapq.heappop(q)
    answer = max(answer,len(q))
print(answer)