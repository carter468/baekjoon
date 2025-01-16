# Game Show
# Gold 4, prefix sum

import sys
input = sys.stdin.readline

N,Q = map(int,input().split())
A = [0]+list(map(int,input().split()))
B = [0]+list(map(int,input().split()))

for i in range(1,N+1):
    if A[i]+B[i] < 0: exit(print(*['flawed' for _ in range(Q)],sep='\n'))
    A[i] += A[i-1]
    B[i] += B[i-1]
if A[-1] < 0 or B[-1] < 0: exit(print(*['flawed' for _ in range(Q)],sep='\n'))

for _ in range(Q):
    a,b = map(int,input().split())

    # 시계방향
    if a <= b:
        l = A[b-1]-A[a-1]
    else:
        l = A[-1]-(A[a-1]-A[b-1])

    # 반시계방향
    if a >= b:
        r = B[a-1]-B[b-1]
    else:
        r = B[-1]-(B[b-1]-B[a-1])
    
    print(min(l,r))