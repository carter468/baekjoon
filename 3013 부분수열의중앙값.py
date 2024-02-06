# 부분 수열의 중앙값
# Gold 3, ad hoc

from collections import defaultdict

n,b = map(int,input().split())
arr = tuple(map(int,input().split()))

idx = arr.index(b)
left,right = defaultdict(int),defaultdict(int)
left[0],right[0] = 1,1
c = 0
for i in range(idx-1,-1,-1):
    if arr[i] > b: c += 1
    else: c -= 1
    left[c] += 1
c = 0
for i in range(idx+1,n):
    if arr[i] > b: c += 1
    else: c -= 1
    right[c] += 1

result = 0
for x in left:
    result += left[x]*right[-x]
print(result)