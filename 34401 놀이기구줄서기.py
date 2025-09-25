# 놀이기구 줄서기
# Gold 5, priority queue

import sys,heapq
input = sys.stdin.readline

N,P,K = map(int,input().split())
arr = [tuple(map(int,input().split())) for _ in range(N)]
heapq.heapify(arr)

result = 0
remain = [[] for _ in range(K)]
t = 0
while arr:
    a,b = heapq.heappop(arr)
    cand = []
    for i in range(b,K):
        while remain[i]:
            x = heapq.heappop(remain[i])
            if a <= x:
                cand.append((x,i))
                break
    if cand:
        cand.sort()
        x,y = cand[0]
        result += x-a
        if y > b:
            heapq.heappush(remain[y-b],x)
        for x,y in cand[1:]:
            heapq.heappush(remain[y],x)
    else:
        if t < a:
            t = ((a-1)//P+1)*P
        result += t-a
        if b < K:
            heapq.heappush(remain[K-b],t)
        t += P
print(result)