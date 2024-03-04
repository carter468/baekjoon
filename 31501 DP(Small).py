# DP (Small)
# Gold 3, LIS

from bisect import bisect_left

n,q = map(int,input().split())
d = tuple(map(int,input().split()))
for _ in range(q):
    a = int(input())-1
    arr = [-1]
    for x in d[:a]:
        if x >= d[a]: continue
        if arr[-1] < x: arr.append(x)
        else: arr[bisect_left(arr,x)] = x
    count = len(arr)
    arr = [-1]
    for x in d[a:]:
        if x <= d[a]: continue
        if arr[-1] < x: arr.append(x)
        else: arr[bisect_left(arr,x)] = x
    count += len(arr)-1
    print(count)