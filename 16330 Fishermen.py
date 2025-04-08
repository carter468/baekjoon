# Fishermen
# Gold 1, binary search, prefix sum

import sys
input = sys.stdin.readline

def find_min(t):
    lo,hi = -1,M
    while lo+1 < hi:
        mid = (lo+hi)//2
        if fisher[mid][0] >= t: hi = mid
        else: lo = mid
    return hi

def find_max(t):
    lo,hi = 0,M
    while lo+1 < hi:
        mid = (lo+hi)//2
        if fisher[mid][0] <= t: lo = mid
        else: hi = mid
    return lo

N,M,L = map(int,input().split())
arr = [tuple(map(int,input().split())) for _ in range(N)]
fisher = []
for i,a in enumerate(map(int,input().split())):
    fisher.append((a,i))
fisher.sort()

result = [0]*(M+1)
for x,y in arr:
    k = L-y
    if k < 0: continue
    l,r = x-k,x+k
    if r < fisher[0][0] or fisher[-1][0] < l: continue
    result[find_min(l)] += 1
    result[find_max(r)+1] -= 1

answer = [0]*M
for i in range(M):
    result[i+1] += result[i]
    answer[fisher[i][1]] = result[i]
print(*answer,sep='\n')