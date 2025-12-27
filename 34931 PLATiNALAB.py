# PLATiNA::LAB
# Gold 2, ad hoc

def f(x):
    if x == 'A': return 'B'
    return 'A'

N,T = map(int,input().split())
S = list(input())

a = [0]*N
c = 0
for i in range(1,N-1):
    if S[i] != S[i-1]:
        c += 1
    else:
        c = 0
    a[i] = c
c = 0
for i in range(N-2,0,-1):
    if S[i] != S[i+1]:
        c += 1
    else:
        c = 0
    a[i] = min(a[i],c)

for i in range(N):
    if min(T,a[i])%2 == 1:
        S[i] = f(S[i])
print(''.join(S))