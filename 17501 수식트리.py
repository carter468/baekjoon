# 수식 트리
# Gold 2, greedy

import sys
input = sys.stdin.readline

N = int(input())
A = [int(input()) for _ in range(N)]
B = [input().split() for _ in range(N-1)]

count = 0
q = [(N*2-2,0)]
while q:
    x,t = q.pop()
    if x < N:
        count += t
    else:
        x -= N
        q.append((int(B[x][1])-1,t))
        if B[x][0] == '-': t ^= 1
        q.append((int(B[x][2])-1,t))

print(sum(A)-sum(sorted(A)[:count])*2)