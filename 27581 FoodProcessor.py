# Food Processor
# Gold 3, greedy, math

import sys,math
input = sys.stdin.readline

S,T,N = map(int,input().split())
blades = sorted([tuple(map(int,input().split())) for _ in range(N)])

if blades[-1][0] < S: exit(print(-1))
result = 0
size = S
t = 10**6
while blades:
    m,h = blades.pop()
    if m < T: break
    if m > size:
        t = min(t,h)
        continue
    result += t*(math.log2(size)-math.log2(m))
    t = min(t,h)
    size = m
result += t*(math.log2(size)-math.log2(T))
print(result)