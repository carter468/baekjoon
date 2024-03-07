# 생일 선물
# Gold 4, two pointer

import sys
input = sys.stdin.readline

n,d = map(int,input().split())
arr = sorted([tuple(map(int,input().split())) for _ in range(n)])

result,x,l,r = 0,0,0,0
while r < n:
    while r < n and arr[l][0]+d > arr[r][0]:
        x += arr[r][1]
        r += 1
    result = max(result,x)
    x -= arr[l][1]
    l += 1
print(result)