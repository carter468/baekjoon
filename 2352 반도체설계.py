# 반도체 설계
# Gold 2, binary search, LIS

import bisect

input()
lis = [0]
for x in map(int,input().split()):
    if lis[-1] < x: lis.append(x)
    else: lis[bisect.bisect_left(lis,x)] = x
print(len(lis)-1)