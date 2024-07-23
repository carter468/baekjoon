# 우체국
# Gold 4, greedy

import sys
input = sys.stdin.readline

arr = []
total = 0
for _ in range(int(input())):
    a,b = map(int,input().split())
    arr.append((a,b))
    total += b
total /= 2
x = 0
for a,b in sorted(arr):
    x += b
    if x >= total:
        print(a)
        break