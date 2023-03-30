# 꼬인 전깃줄
# Gold 2, LIS

from bisect import bisect_left

n = int(input())
arr = tuple(map(int,input().split()))

result = [arr[0]]
for i in range(1,n):
    if (idx:=bisect_left(result,arr[i])) == len(result):
        result.append(arr[i])
    else:
        result[idx] = arr[i]

print(n-len(result))