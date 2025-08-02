# 벨과 와이즈의 가게 홍보
# Gold 3, permutation cycle decomposition

N = int(input())
A = tuple(map(int,input().split()))

B = [0]+list(A)
idx = [0]*(N+1)
for i in range(1,N+1):
    idx[B[i]] = i
c1 = 0
for i in range(1,N+1):
    if idx[i] == i: continue
    c1 += 1
    idx[B[i]],B[idx[i]] = idx[i],B[i]

B = [0]+list(A)
idx = [0]*(N+1)
for i in range(1,N+1):
    idx[B[i]] = i
c2 = 0
for i in range(1,N+1):
    if idx[i] == N+1-i: continue
    c2 += 1
    idx[B[N+1-i]],B[idx[i]] = idx[i],B[N+1-i]

print(N-2,min(c1,c2))