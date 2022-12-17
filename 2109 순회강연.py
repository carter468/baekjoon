# 순회강연
# Gold 3, 그리디 알고리즘, 우선순위 큐

import sys
input = sys.stdin.readline
import heapq

n = int(input())
offer = []
for _ in range(n):
    p,d = map(int,input().split())
    heapq.heappush(offer,(-p,d))

pay = 0
schedule = [False]*10001
for _ in range(n):
    p,d = heapq.heappop(offer)
    for i in range(d,0,-1):
        if not schedule[i]:
            schedule[i] = True
            pay -= p
            break

print(pay)