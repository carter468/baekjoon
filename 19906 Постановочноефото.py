# Постановочное фото
# Platinum 5, constructive, greedy

M,N = map(int,input().split())
A = tuple(map(int,input().split()))

last_pos = [-1]*(N+1)
for i in range(M):
    last_pos[A[i]] = i

q = []
for i in range(M):
    j = last_pos[A[i]]
    if j != -1:
        q.append((A[i],i+1,j+1))
        last_pos[A[i]] = -1

arr = [0]*M
jump = [-1]*(M)
for c,i,j in q[::-1]:
    i -= 1
    j -= 1
    s,e = i,j
    while i <= j:
        if jump[i] == -1:
            arr[i] = c
        else:
            i = jump[i]
        i += 1
    jump[s] = e

for i in range(M):
    if A[i] != arr[i]:
        print(-1)
        break
else:
    print(len(q))
    for a in q:
        print(*a)