# 교도소
# Gold 4, simulation

N = int(input())
A = tuple(map(int,input().split()))

m = sum(A)//N

a,x = 0,-1
count = 0
for i in range(N):
    count += a
    a += A[i]-m
    if a < 0:
        count = 0
        a = 0
        x = i
    elif a > 0:
        y = i

if x != -1:
    while x != y:
        count += a
        y = (y+1)%N
        a += A[y]-m
print(count)