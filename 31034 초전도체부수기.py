# 초전도체 부수기
# Platinum 3, priority queue, greedy

from collections import defaultdict
import sys,heapq
input = sys.stdin.readline

for _ in range(int(input())):
    N,K = map(int,input().split())

    count = defaultdict(int)
    count[1] = K-1
    count[N-K+1] += 1
    q = list(count.keys())
    heapq.heapify(q)
    result = 0
    while sum(count.values()) > 1:
        val = q[0]
        c = count[val]
        if c > 1:
            a,count[val] = divmod(c,2)
            if count[val] == 0: 
                heapq.heappop(q)
            if val*2 not in count:
                heapq.heappush(q,val*2)
            count[val*2] += a
            result += a*val*2
        else:
            count[val] = 0
            heapq.heappop(q)
            val2 = q[0]
            count[val2] -= 1
            if count[val2] == 0:
                heapq.heappop(q)
            if val+val2 not in count:
                heapq.heappush(q,val+val2)
            count[val+val2] += 1
            result += val+val2
    print(result)