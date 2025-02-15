# 속타는 저녁 메뉴
# Platinum 5, KMP

def gcd(a,b):
    while b: 
        a,b = b,a%b
    return a

N = int(input())
S = list(input().split())
T = list(input().split())

T += T[:-1]
M = N*2-1

pi = [0]*N
i = 0
for j in range(1,N):
    while i > 0 and S[i] != S[j]:
        i = pi[i-1]
    if S[i] == S[j]:
        i += 1
        pi[j] = i

c = 0
i = 0
for j in range(M):
    while i > 0 and S[i] != T[j]:
        i = pi[i-1]
    if S[i] == T[j]:
        i += 1
        if i == N:
            c += 1
            i = pi[i-1]

g = gcd(N,c)
print(f'{c//g}/{N//g}')