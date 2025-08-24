# 마을 짓기
# Gold 2, prefix sum, two pointer

import sys
input = sys.stdin.readline

N,M = map(int,input().split())
A = [input() for _ in range(N)]

psum = [[0]*(M+1) for _ in range(N+1)]
for i in range(N):
    for j in range(M):
        psum[i][j] = psum[i-1][j]+psum[i][j-1]-psum[i-1][j-1]
        if A[i][j] == 'X':
            psum[i][j] += 1

count = [0]*min(N,M)
for j in range(M):
    i = 0
    ii,jj = i,j
    k = 0
    while i < N and j < M:
        if A[ii][jj] == 'X':
            if psum[ii][jj]-psum[ii][j-1]-psum[i-1][jj]+psum[i-1][j-1] == ii-i+1:
                k = ii-i+1
                if ii == N-1 or jj == M-1:
                    for a in range(k):
                        count[a] += 1
                    break
                else:
                    ii += 1
                    jj += 1
            else:
                if k > 0: count[k-1] += 1
                i += 1
                j += 1
                k -= 1
        else:
            for a in range(k):
                count[a] += 1
            ii += 1
            jj += 1
            i,j = ii,jj
            k = 0

for i in range(1,N):
    j = 0
    ii,jj = i,j
    k = 0 
    while i < N and j < M:
        if A[ii][jj] == 'X':
            if psum[ii][jj]-psum[ii][j-1]-psum[i-1][jj]+psum[i-1][j-1] == ii-i+1:
                k = ii-i+1
                if ii == N-1 or jj == M-1:
                    for a in range(k):
                        count[a] += 1
                    break
                else:
                    ii += 1
                    jj += 1
            else:
                if k > 0:
                    count[k-1] += 1
                i += 1
                j += 1
                k -= 1
        else:
            for a in range(k):
                count[a] += 1
            ii += 1
            jj += 1
            i,j = ii,jj
            k = 0

for i in range(len(count)-1):
    count[-2-i] += count[-1-i]
print(*count,sep='\n')