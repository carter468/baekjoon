# 카드 게임 (Hard)
# Gold 3, greedy, priority queue

import sys,heapq
input = sys.stdin.readline

H = int(input())
N,Q = map(int,input().split())
D = sorted(map(int,input().split()))

heap = []
t = 0
count = 0
while D:
    x = D.pop()
    heapq.heappush(heap,x)
    t += x
    count += 1
    if t >= H:
        print(count)
        break
else: print(-1)

for _ in range(Q):
    x = int(input())
    heapq.heappush(heap,x)
    t += x
    count += 1
    if t < H:
        print(-1)
    else:
        while t >= H:
            if t-heap[0] >= H:
                t -= heapq.heappop(heap)
                count -= 1
            else: break
        print(count)