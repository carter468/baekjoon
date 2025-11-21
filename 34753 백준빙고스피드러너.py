# 백준 빙고 스피드러너
# Gold 3, impelmentation, simulation

import sys
input = sys.stdin.readline
INF = 10**15

N = int(input())
A = [list(map(int,input().split())) for _ in range(N)]

remain = []
a,b = 0,0
for i in range(N):
    remain.append([0,i,sum(A[i])])
for i in range(N):
    x = 0
    for j in range(N):
        x += A[j][i]
    remain.append([1,i,x])
    a += A[i][i]
    b += A[i][-1-i]
remain.append([2,2,a])
remain.append([3,3,b])

M = N*2+2
result = [0]*M
k = 0
p = 0
while True:
    minv,t,idx = INF,None,None
    k = 0
    for i in range(M):
        if remain[i][2] > 0:
            x,y,z = remain[i]
            if z < minv: minv,t,idx = z,x,y
        else:
            k += 1
    if k == M: break
    p += minv
    result[k] = p

    if t == 0:
        for i in range(N):
            if A[idx][i] > 0:
                remain[i+N][2] -= A[idx][i]
                if idx == i:
                    remain[-2][2] -= A[idx][i]
                if idx+i+1 == N:
                    remain[-1][2] -= A[idx][i]
                A[idx][i] = 0
        remain[idx][2] = 0
    elif t == 1:
        for i in range(N):
            if A[i][idx] > 0:
                remain[i][2] -= A[i][idx]
                if idx == i:
                    remain[-2][2] -= A[i][idx]
                if idx+i+1 == N:
                    remain[-1][2] -= A[i][idx]
                A[i][idx] = 0
        remain[idx+N][2] = 0
    elif t == 2:
        for i in range(N):
            if A[i][i] > 0:
                remain[i][2] -= A[i][i]
                remain[i+N][2] -= A[i][i]
                if i+i+1 == N:
                    remain[-1][2] -= A[i][i]
                A[i][i] = 0
        remain[-2][2] = 0
    elif t == 3:
        for i in range(N):
            if A[-1-i][i] > 0:
                remain[N-1-i][2] -= A[-1-i][i]
                remain[i+N][2] -= A[-1-i][i]
                if i+i+1 == N:
                    remain[-2][2] -= A[-1-i][i]
                A[-1-i][i] = 0
        remain[-1][2] = 0
    
for i in range(M):
    if result[i] == 0:
        result[i] = result[i-1]
print(*result,sep='\n')