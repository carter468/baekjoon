# 키가 비슷한 친구
# Gold 2, priority queue

import heapq

for tc in range(int(input())):
    N,K = map(int,input().split())
    arr = sorted([(x,i) for i,x in enumerate(map(int,input().split()))])

    result = 0
    heap = []
    for x,i in arr:
        heapq.heappush(heap,(i,x))
        while heap[0][1] < x-K:
            heapq.heappop(heap)
        result += i-heap[0][0]
    print(f'Case #{tc+1}')
    print(result)