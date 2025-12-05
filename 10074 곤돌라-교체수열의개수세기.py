# 곤돌라 - 교체 수열의 개수 세기
# Platinum 4, combinatorics, exponentiation by squaring

MOD = 10**9+9

N = int(input())
A = tuple(map(int,input().split()))

arr = set()
s = None
for i in range(N):
    if A[i] <= N:
        s = i
    elif A[i] in arr:
        exit(print(0))
    else:
        arr.add(A[i])
for i in range(N):
    if A[i] <= N and (A[i]-A[s])%N != (i-s)%N:
        exit(print(0))

result = 1 if s else N
c = len(arr)
p = N
for a in sorted(arr):
    result = result*pow(c,a-p-1,MOD)%MOD
    c -= 1
    p = a
print(result)