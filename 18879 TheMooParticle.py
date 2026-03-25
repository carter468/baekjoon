# The Moo Particle
# Platinum 5, sweeping

import sys
input = sys.stdin.readline
INF = 10**9

N = int(input())
A = sorted([tuple(map(int,input().split())) for _ in range(N)])

L = [INF]*N
R = [-INF]*(N+1)
for i in range(N):
    L[i] = min(L[i-1],A[i][1])
for i in range(N-1,-1,-1):
    R[i] = max(R[i+1],A[i][1])

count = 1
for i in range(N-1):
    if L[i] > R[i+1]:
        count += 1
print(count)