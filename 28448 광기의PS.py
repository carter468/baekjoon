# 광기의 PS
# Platinum 5, greedy

import sys
input = sys.stdin.readline

N,L = map(int,input().split())

arr = []
result = 0
for _ in range(N):
    k,t = map(int,input().split())
    result += t
    if t > 5:
        arr.append((-k,k*(t-5),k*t)) 

x = 0 
for k,a,b in sorted(arr):
    if x+b > L:
        f = x+b-L
        result += f
        x -= f
    x += a
print(result)