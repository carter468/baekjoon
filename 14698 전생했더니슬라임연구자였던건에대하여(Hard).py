# 전생했더니 슬라임 연구자였던 건에 대하여 (Hard)
# Gold 4, 그리디, 우선순위큐

import sys,heapq
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    e = list(map(int,input().split()))
    
    heapq.heapify(e)
    result = 1
    while len(e) > 1:
        a,b = heapq.heappop(e),heapq.heappop(e)
        result = result*a*b%(10**9+7)
        heapq.heappush(e,a*b)
    print(result)