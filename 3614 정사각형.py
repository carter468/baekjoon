# 정사각형
# Gold 2, number theory

import math

N = int(input())

s = set()
for i in range(1,int(N**0.5)+1):
    if N%i == 0:
        s.add(i+1)
        s.add(N//i+1)

count = 0
for x in s:
    for i in range(x//2+1):
        count += (math.gcd(i,x-i) == 1)
print(count)