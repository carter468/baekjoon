# 행성 X3
# Gold 3, math, bitmasking

import sys
input = sys.stdin.readline

count = [0]*20
n = int(input())
for _ in range(n):
    a = int(input())
    for i in range(20):
        if a&(1<<i): count[i] += 1

result = 0
for i in range(20):
    result += 2**i*(count[i]*(n-count[i]))
print(result)