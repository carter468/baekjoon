# 극적인 승리
# Gold 4, binary search

from collections import defaultdict
import sys,bisect
input = sys.stdin.readline

A,B = map(int,input().split())
if A < B: exit(print(-1,-1))
N = int(input())
arr = [tuple(map(int,input().split())) for _ in range(N)]

right = []
count = defaultdict(list)
for i in range(N):
    _,r = arr[i]
    right.append(r)
    count[r].append(i)
right.sort()

result = [10**9]
for i in range(N+1):
    if i == N:
        i,l = -2,0
    else:
        l,_ = arr[i]
    t = A-B-l
    if t < 0:
        if B+l-A < result[0]:
            result = [B+l-A,i+1,-1]
        continue
    a = bisect.bisect_right(right,t)
    if a != N:
        b = right[a]
        s = l+b+B
        if A < s and s-A < result[0]:
            for j in count[b]:
                if i != j:
                    result = [s-A,i+1,j+1]
                    break
            else:
                if a+1 != N:
                    b = right[a+1]
                    s = l+b+B
                    if s-A < result[0]:
                        result = [s-A,i+1,count[b][0]+1]

if result[0] == 10**9: print('No')
else: print(*result[1:])