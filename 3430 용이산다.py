# 용이 산다
# Gold 1, greedy, priority queue

import heapq

def solve():
    N,M = map(int,input().split())
    T = tuple(map(int,input().split()))

    next_idx = [-1]*M
    prev_idx = dict()
    empty = [False]*(N+1)
    q = []
    for i,t in enumerate(T):
        if t != 0:
            if t in prev_idx:
                next_idx[prev_idx[t]] = i
            else:
                heapq.heappush(q,i)
            prev_idx[t] = i
    
    result = []
    for i,t in enumerate(T):
        if t == 0:
            if q:
                idx = heapq.heappop(q)
                result.append(T[idx])
                empty[T[idx]] = True
            else:
                result.append(0)
        else:
            if not empty[t]:
                print('NO')
                return
            empty[t] = False
            if next_idx[i] != -1:
                heapq.heappush(q,next_idx[i])

    print('YES')
    print(*result)
    return

for _ in range(int(input())):
    solve()