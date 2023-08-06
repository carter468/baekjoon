# 도둑
# Gold 4, two pointer, sliding window

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n,m,k = map(int,input().split())
    arr = tuple(map(int,input().split()))
    l,r = n-m,n
    x = sum(arr[l:r])
    result = 0
    if x < k: result += 1
    if n != m:
        while r > 1:
            l -= 1
            r -= 1
            x += arr[l]-arr[r]
            if x < k: result += 1
    print(result)