# 자르기
# Gold 1, ad hoc

N = int(input())
A = tuple(map(int,input().split()))

L = [10**9]*N
m = 0
for i,a in enumerate(A):
    m = max(m,a)
    L[i] = min(A[0],a)+m

R = [10**9]*N
m = 0
for i in range(N-1,-1,-1):
    a = A[i]
    m = max(m,a)
    R[i] = min(A[-1],a)+m

result = 10**9
for i in range(1,N-2):
    result = min(result,L[i]+R[i+1])
print(result)