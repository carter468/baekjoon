# 챔피언 (Easy)
# Gold 1, ad hoc

N = int(input())
A = tuple(map(int,input().split()))

result = []
m = 0
for i in range(N-1,-1,-1):
    a = A[i]
    if a != A[i-1] and a > m:
        result.append(i+1)
    m = max(m,a-i+1)

if N == 1: result = [1]
print(*result[::-1] if result else [-1])