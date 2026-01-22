# 견제 미로찾기
# Gold 1, DP, game theory

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def f(x,y,k):
    if (x,y,k) in dp:
        return dp[(x,y,k)]

    if k > 1:
        if f(x,y,1) == 0:
            dp[(x,y,k)] = 1
            return 1

    for i in range(2,int(k**0.5)+1):
        if k%i == 0:
            if f(x,y,i) == 0:
                dp[(x,y,k)] = 1
                return 1
            if f(x,y,k//i) == 0:
                dp[(x,y,k)] = 1
                return 1

    for i in range(1,k+1):
        nx = x+i
        if nx == N or A[nx][y] == 1: break
        if f(nx,y,k) == 0:
            dp[(x,y,k)] = 1
            return 1

    for i in range(1,k+1):
        ny = y+i
        if ny == N or A[x][ny] == 1: break
        if f(x,ny,k) == 0:
            dp[(x,y,k)] = 1
            return 1

    dp[(x,y,k)] = 0
    return 0

N,K = map(int,input().split())
A = [tuple(map(int,input().split())) for _ in range(N)]

dp = dict()
print(f(0,0,K))