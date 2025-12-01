# 매드 맥스
# Gold 3, ad hoc

input()
A = sorted(map(int,input().split()))

x1 = max(A)+(min(A)==0)
for i,a in enumerate(A):
    if i != a: break
if A[i] == i: i += 1
x2 = i+A[len(A)//2]

print(max(x1,x2))