# 용액 합성하기
# Gold 5, two pointer

N = int(input())
A = sorted(map(int,input().split()))

result = A[0]+A[-1]
l,r = 0,N-1
while l < r:
    x = A[l]+A[r]
    if abs(x) < abs(result): result = x
    if x > 0: r -= 1
    else: l += 1
print(result)