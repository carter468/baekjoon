# 행렬 연산 (연산 찾기)
# Platinum 5, ad hoc, constructive

from collections import defaultdict
import sys
input = sys.stdin.readline

N,M = map(int,input().split())
arr = [tuple(map(int,input().split())) for _ in range(N)]

count = defaultdict(int)
R = [0]*N
C = [0]*M
for j in range(M):
    C[j] = arr[0][j]
    count[C[j]] += 1
for i in range(N):
    R[i] = arr[i][0]-C[0]
    count[-R[i]] += 1
m = max(count,key=count.get)

for i in range(N):
    for j in range(M):
        if R[i]+C[j] != arr[i][j]:
            exit(print(-1))

print(N+M-count[m])
for i in range(N):
    v = R[i]+m
    if v != 0: print(1,i+1,v)
for j in range(M):
    v = C[j]-m
    if v != 0: print(2,j+1,v)