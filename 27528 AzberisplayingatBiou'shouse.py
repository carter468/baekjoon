# Azber is playing at Biou's house
# Gold 1, DP, game theory

import sys
sys.setrecursionlimit(1111)

def solve(i,j,k):
    if dp[i][j][k] != None: return dp[i][j][k]
    if i == 1: return A[i-1]

    arr = [0]
    nj = j^1
    ni = i-1
    if i.bit_length() == ni.bit_length() and k != 1:
        arr.append(solve(ni,nj,2))
    ni = i+1
    if i.bit_length() == ni.bit_length() and k != 2:
        arr.append(solve(ni,nj,1))
    arr.append(solve(i//2,nj,0))

    if j == 0: v = min(arr)
    else: v = max(arr)

    dp[i][j][k] = A[i-1]+v
    return dp[i][j][k]

N = int(input())
A = tuple(map(int,input().split()))

# i번방에 a턴일때 얻는 최소점수, b턴일때 얻는 최대점수
# 0:전위치가 좌우가아님, 1: 전위치가 좌, 2: 전위치가 우
dp = [[[None,None]*3 for _ in range(2)] for _ in range(1<<N)]
result = []
for i in range(1,1<<N):
    result.append(solve(i,0,0))
print(*result)