# 대칭 XOR
# Gold 4, ad hoc

N = int(input())
if N == 1: exit(print(1))
if N%2 == 1: exit(print(-1))

count = [0]*20
for i in range(1,N+1):
    for j in range(20):
        if i>>j&1: count[j] += 1

for i in range(20):
    if count[i] != 0 and count[i]*2 != N:
        print(-1)
        break
else:
    print(*range(1,N+1))

# ------------------------
N = int(input())

a = 2
while a < N:
    a = a*2+2

if a == N or a == 2: print(*range(1,N+1))
else: print(-1)