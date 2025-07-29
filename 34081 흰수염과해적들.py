# 흰수염과 해적들
# Gold 1, priority queue, greedy

import sys,heapq
input = sys.stdin.readline

N,L = map(int,input().split())
pirate = []
for _ in range(N):
    x,y,c = map(int,input().split())
    r = x*x+y*y
    d = int(r**0.5)
    if d*d < r: d += 1
    if d <= L: pirate.append((d,c))
pirate.sort()

heap = []
while pirate:
    a = pirate[-1][0]
    while pirate and pirate[-1][0] == a:
        heapq.heappush(heap,pirate.pop()[1])
    while len(heap) > L-a+1:
        heapq.heappop(heap)
print(sum(heap))