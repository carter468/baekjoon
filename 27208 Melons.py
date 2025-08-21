# Melons
# Gold 2, two pointer, DP

import sys
input = sys.stdin.readline

N,L = map(int,input().split())
A = [int(input()) for _ in range(N)]

end = [0]*N
w = [0]*N
r = 0
t = 0
for i in range(N):
    while r < N and t+A[r] <= L:
        t += A[r]
        r += 1
    end[i] = r-1
    w[i] = t
    t -= A[i]

result = [[0]*2 for _ in range(N)]
for i in range(N-1,-1,-1):
    if end[i] == N-1:
        result[i] = [1,w[i]]
    else:
        j = end[i]+1
        result[i] = [1+result[j][0],result[j][1]]

for i in range(N):
    print(*result[i])