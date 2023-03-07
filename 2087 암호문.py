# 암호문
# Gold 1, 비트마스킹, 중간에서 만나기

import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    arr = [int(input()) for _ in range(n)]
    k = int(input())

    mid = n//2
    result = {}
    for i in range(1<<mid):
        t = 0
        for j in range(mid):
            if i&(1<<j):
                t += arr[mid-j-1]
        result[t] = i

    for i in range(1<<n-mid):
        t = 0
        for j in range(n-mid):
            if i&(1<<j):
                t += arr[n-j-1]
        if k-t in result:
            return bin(result[k-t])[2:].zfill(mid)+bin(i)[2:].zfill(n-mid)

print(solve())