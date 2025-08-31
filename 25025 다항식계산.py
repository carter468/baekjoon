# 다항식 계산
# Platinum 5, math, FLT

N,P = map(int,input().split())
A = tuple(map(int,input().split()))

p = P-1
arr = [0]*p
for i in range(N):
    arr[(N-i)%p] += A[i]

print(A[-1]%P)
arr[0] += A[-1]
for i in range(1,P):
    t = 0
    k = 1
    for j in range(p):
        t += arr[j]*k
        k = k*i%P
    print(t%P)