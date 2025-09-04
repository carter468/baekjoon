# 토너먼트
# Gold 2, greedy, bitmask

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    a,b = map(int,input().split())

    x = a
    count = 0
    i = 1
    while x > 2:
        if x%2 == 1:
            if a+i > b: count += 1
            else: a += i
        x = (x+1)>>1
        i <<= 1
    print(count)