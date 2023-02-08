# 아우으 우아으이야!!
# Gold 5, 스위핑

import sys
input = sys.stdin.readline

N = int(input())
result = 0
left,right = map(int,input().split())
for _ in range(N-1):
    x,y = map(int,input().split())
    if x > right:
        result += right-left
        left,right = x,y
    elif y > right:
        right = y
print(result+right-left)