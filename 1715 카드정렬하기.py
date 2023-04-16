# 카드 정렬하기
# Gold 4, 그리디, 우선순위큐

import sys,heapq
input = sys.stdin.readline

n = int(input())
result = 0
heapq.heapify(q:=[int(input()) for _ in range(n)])
for _ in range(n-1):
    heapq.heappush(q,(c:=heapq.heappop(q)+heapq.heappop(q)))
    result += c

print(result)