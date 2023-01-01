# 나무 막대
# Gold 2, 우선순위 큐

import sys
import heapq
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    data = tuple(map(int,input().split()))
    wood = []
    for i in range(n):
        heapq.heappush(wood,(data[i*2],data[i*2+1]))

    count = 0
    while wood:
        count += 1
        cl,cw = heapq.heappop(wood)
        next_work = []
        while wood:
            nl,nw = heapq.heappop(wood)
            if cl<=nl and cw<=nw:
                cl,cw = nl,nw
            else:
                heapq.heappush(next_work,(nl,nw))
        wood = next_work
    print(count)