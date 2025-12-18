# 행렬의 텐서곱
# Platinum 4, implementation, number theory

import sys
input = sys.stdin.readline

def gcd(a,b):
    while b:
        a,b = b,a%b
    return a

def count(r,c):
    g = M[0][0]
    for i in range(r):
        for j in range(c):
            g = gcd(g,M[i][j])
    
    A = [[0]*c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            A[i][j] = M[i][j]//g
    
    B = [[0]*(C//c) for _ in range(R//r)]
    for i in range(R):
        for j in range(C):
            x,y = i%r,j%c
            if M[i][j]%A[x][y] != 0: return 0
            z = B[i//r][j//c]
            if z == 0:
                B[i//r][j//c] = M[i][j]//A[x][y]
            elif z != M[i][j]//A[x][y]:
                return 0

    g = B[0][0]
    for i in range(R//r):
        for j in range(C//c):
            g = gcd(g,B[i][j])

    k = 0
    for i in range(1,int(g**0.5)+1):
        if g%i == 0:
            k += 1
            if i*i != g:
                k += 1
    return k

while True:
    R,C = map(int,input().split())
    if R == 0: break

    M = [tuple(map(int,input().split())) for _ in range(R)]

    result = 0
    for i in range(1,R+1):
        if R%i == 0:
            for j in range(1,C+1):
                if C%j == 0 and (i != 1 or j != 1) and (i != R or j != C):
                    result += count(i,j)

    print(result)