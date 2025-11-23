# Karamell
# Gold 3, DP, knapsack, traceback

N = int(input())
A = tuple(map(int,input().split()))

s = sum(A)
if s%2: exit(print(-1))

M = s//2
dp = [[False]*(M+1) for _ in range(N+1)]
dp[0][0] = True
for i in range(N):
    a = A[i]
    for j in range(M+1):
        if dp[i][j]:
            dp[i+1][j] = True
            if j+a <= M:
                dp[i+1][j+a] = True

if not dp[N][M]: exit(print(-1))
arr1,arr2 = [],[]
for i in range(N-1,-1,-1):
    a = A[i]
    if dp[i][M]:
        arr1.append(a)
    else:
        arr2.append(a)
        M -= a

result = []
x = 0
while arr1 or arr2:
    if x > 0:
        a = arr2.pop()
        x -= a
    else:
        a = arr1.pop()
        x += a
    result.append(a)
print(*result)