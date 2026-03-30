# 관광 상품
# Gold 2, ad hoc

N = int(input())
A = tuple(map(int,input().split()))

m = min(A[:2])
for i in range(2,N):
    m = max(m,min(A[i-1],A[i]),sorted(A[i-2:i+1])[1])
print(m)