# 로마의 휴일
# Gold 5, two pointer

N,K,X = map(int,input().split())
A = tuple(map(int,input().split()))

result = -1
total = sum(A)-A[0]
l,r = 0,0
while r < N:
    if total >= K:
        result = max(result,r-l+1)
        r += 1
        if r < N:
            total -= A[r]
    else:
        total += A[l]*X
        l += 1
        if l > r:
            r = l
            if r < N: total -= A[r]
print(result)