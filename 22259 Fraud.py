# Fraud
# Gold 2, math

N = int(input())
A = tuple(map(int,input().split()))
B = tuple(map(int,input().split()))

result = 'YES'
l,r = 10**9,0
for i in range(N-1):
    a1,a2,b1,b2 = A[i],A[i+1],B[i],B[i+1]
    if a1 <= a2 and b1 <= b2:
        result = 'NO'
        break
    if (a1 >= a2 and b1 > b2) or (a1 > a2 and b1 >= b2): continue
    m = (a1-a2)/(b2-b1)
    if b2 > b1: l = min(l,m)
    else: r = max(r,m)
if l <= r: result = 'NO'
print(result)