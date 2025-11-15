# 세미-연속 수열
# Gold 3, sliding window

N,K = map(int,input().split())
P = tuple(map(int,input().split()))

count = 0
arr = [False]*(N+2)
for i in range(K):
    a = P[i]
    if arr[a-1]: count += 1
    if arr[a+1]: count += 1
    arr[a] = True
if count == K-1:
    print('YES')
    print(*P[:K])
    exit()

for i in range(N-K):
    a = P[i]
    b = P[i+K]
    if arr[a-1]: count -= 1
    if arr[a+1]: count -= 1
    arr[a] = False
    if arr[b-1]: count += 1
    if arr[b+1]: count += 1
    arr[b] = True
    if count == K-1:
        print('YES')
        print(*P[i+1:i+K+1])
        exit()
print('NO')