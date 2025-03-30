# Chessboard
# Gold 1, math, derangement

N,M = map(int,input().split())

result = 0
n = 1
for i in range(N+1):
    if (N-i)%2 == 0: result += n
    else: result -= n
    n = n*(N-i)%M
    if n == 0: break
print(result**2%M)