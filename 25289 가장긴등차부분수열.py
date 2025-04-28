# 가장 긴 등차 부분 수열
# Gold 4, bruteforcing, binary search

import bisect
M = 100

input()
arr = [[] for _ in range(M+1)]
for i,a in enumerate(map(int,input().split())):
    arr[a].append(i)

result = 0
for d in range(-M,M): # 공차
    for i in range(1,M+1): # 첫 항
        length = 0
        k = -1
        while 0 < i < M+1 and arr[i] and arr[i][-1] > k:
            k = arr[i][bisect.bisect_left(arr[i],k+1)]
            i += d
            length += 1
        result = max(result,length)
print(result)