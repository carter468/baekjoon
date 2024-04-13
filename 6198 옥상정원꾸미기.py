# 옥상 정원 꾸미기
# Gold 5, priority queue

import sys,heapq
input = sys.stdin.readline

result = 0
q = []
n = int(input())
for i in range(n):
    h = int(input())
    while q and q[0][0] <= h:
        a,b = heapq.heappop(q)
        result += i-b-1
    heapq.heappush(q,(h,i))
while q:
    result += n-heapq.heappop(q)[1]-1
print(result)