# 둘이 한 팀
# Gold 1, binary search, prefix sum

import sys
input = sys.stdin.readline

N = int(input())
arr = []
for _ in range(N):
    a,b = map(int,input().split())
    arr.append((a-b,a,b))
arr.sort()

sumA,sumB = [0],[0]
for _,a,b in arr:
    sumA.append(sumA[-1]+a)
    sumB.append(sumB[-1]+b)

pa = pb = 0
for _ in range(int(input())):
    i,x = input().split()
    if i == 'A': pa += int(x)
    else: pb += int(x)

    c = pb-pa
    lo,hi = -1,N
    while lo+1 < hi:
        mid = (lo+hi)//2
        if arr[mid][0] > c: hi = mid
        else: lo = mid
    
    result = sumA[-1]-sumA[hi]+sumB[hi]+pa*(N-hi)+pb*hi
    print(result)