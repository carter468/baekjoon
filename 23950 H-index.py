# H-index
# Gold 4, priority queue, ad hoc

import heapq

for t in range(int(input())):
    input()
    q = []
    result = []
    h = 0
    for a in map(int,input().split()):
        if a >= h:
            heapq.heappush(q,a)
            while q and q[0] < len(q):
                heapq.heappop(q)
            h = max(h,min(q[0],len(q)))
        result.append(h)
    print(f'Case #{t+1}:',*result)