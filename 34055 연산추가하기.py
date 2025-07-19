# 연산 추가하기
# Gold 2, binary search, prefix sum, sweeping

import sys,bisect
input = sys.stdin.readline

N,H = map(int,input().split())
arr = sorted([tuple(map(int,input().split())) for _ in range(N)])

e = []
r = 0
for a,b in arr:
    if a > r: e.append(a-r-1)
    r = max(r,b)
e.append(H-r)
e.sort()
n = len(e)

psum = [0]
for x in e:
    psum.append(psum[-1]+x)

result = []
for _ in range(int(input())):
    t = int(input())
    idx = bisect.bisect_left(e,t)
    result.append(psum[-1]-psum[idx]-(t-1)*(n-idx))
print(*result,sep='\n')