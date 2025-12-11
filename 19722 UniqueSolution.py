# Unique Solution
# Platinum 5, constructive, math

N = int(input())
A = tuple(map(int,input().split()))

x = [0]*N
a = 1
for i in range(N):
    if A[i] == 0:
        x[i] = a
        a <<= 1

m = 0
for i in range(N):
    if A[i] > 0:
        x[i] = a
        m += a
        a <<= 1
    elif A[i] < 0:
        x[i] = -a
        m += a
        a <<= 1

print(m)
print(*x)