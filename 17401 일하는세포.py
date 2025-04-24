# 일하는 세포
# Platinum 5, exponentiation by squaring

import sys
input = sys.stdin.readline
MOD = 10**9+7

def mul(A,B):
    result = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            t = 0
            for k in range(N):
                t += A[i][k]*B[k][j]
            result[i][j] = t%MOD
    return result

def pow(A,p):
    if p == 0:
        return [[1 if i == j else 0 for j in range(N)] for i in range(N)]
    if p == 1: return A

    B = pow(A,p//2)
    if p%2 == 0: return mul(B,B)
    else: return mul(mul(B,B),A)

T,N,D = map(int,input().split())
if D == 0:
    for _ in range(N):
        print(*[0]*N)
    exit()
arr = [[[0]*N for _ in range(N)] for _ in range(T)]
for i in range(T):
    for _ in range(int(input())):
        a,b,c = map(int,input().split())
        arr[i][a-1][b-1] = c

arr1 = [[1 if i == j else 0 for j in range(N)] for i in range(N)]
for i in range(T):
    arr1 = mul(arr1,arr[i])
arr2 = [[1 if i == j else 0 for j in range(N)] for i in range(N)]
for i in range(D%T):
    arr2 = mul(arr2,arr[i])

answer = mul(pow(arr1,D//T),arr2)
for a in answer:
    print(*a)