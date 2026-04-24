# 순환 순열
# Platinum 5, KMP

A,B = input(),input()*2

N = len(A)
pi = [0]*N
i = 0
for j in range(1,N):
    while i > 0 and A[i] != A[j]:
        i = pi[i-1]
    if A[i] == A[j]:
        i += 1
        pi[j] = i

count = 0
i = 0
for j in range(N*2-1):
    while i > 0 and A[i] != B[j]:
        i = pi[i-1]
    if A[i] == B[j]:
        i += 1
        if i == N:
            count += 1
            i = pi[i-1]
print(count)