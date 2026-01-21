# Mendelian Genetics
# Gold 2, priority queue

import sys,heapq
input = sys.stdin.readline

for ds in range(int(input())):
    N = int(input())
    A = sorted(map(int,input().split()))

    result = []
    used = {(N-1,N-1)}
    heap = [(-A[-1],N-1,N-1)]
    for _ in range(N):
        x,i,j = heapq.heappop(heap)
        result.append(-x)
        for ni,nj in (i-1,j),(i,j-1):
            if (ni,nj) not in used:
                used.add((ni,nj))
                heapq.heappush(heap,(-((A[ni]+A[nj]+1)//2),ni,nj))

    print(f'Data Set {ds+1}:')
    print(*result,'\n')