# PIN
# Platinum 3, combinatorics, inclusion and exclusion

import sys
input = sys.stdin.readline
M = 37

dic = {chr(i+97):i+10 for i in range(26)}
for i in range(10):
    dic[str(i)] = i

N,D = map(int,input().split())

C = [[[[0]*M for _ in range(M)] for _ in range(M)] for _ in range(M)]
for _ in range(N):
    s = input()
    for i in range(1<<4):
        a,b,c,d = [dic[s[j]] if i>>j&1 else 36 for j in range(4)]
        C[a][b][c][d] += 1

T = [0]*5
for a in range(M):
    for b in range(M):
        for c in range(M):
            for d in range(M):
                x = C[a][b][c][d]
                k = [a,b,c,d].count(36)
                T[k] += x*(x-1)//2

print([0,T[1],T[2]-T[1]*3,T[3]-T[2]*2+T[1]*3,N*(N-1)//2-T[1]+T[2]-T[3]][D])