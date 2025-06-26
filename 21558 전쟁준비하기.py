# 전쟁 준비하기
# Gold 5, math

N = int(input())
A = tuple(map(int,input().split()))

t = sum(A)
result = [0]*N
arr = set()
for i in range(1,int(t**0.5)+1):
    if t%i == 0:
        arr.add(i)
        arr.add(t//i)

e = N
for y in sorted(arr,reverse=True):
    c = 0
    r = 0
    for a in A:
        r = (a+r)%y
        if r != 0: c += 1
    for i in range(c,e):
        result[i] = max(result[i],y)
    e = c
print(*result)