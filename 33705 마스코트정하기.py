# 마스코트 정하기
# Gold 5, ad hoc

N = int(input())
arr = tuple(map(int,input().split()))

C = arr.count(1)
if C*2 >= N: exit(print(0))

c = 0
for i in range(N):
    if arr[i] == 1: c += 1
    if c*2 >= i+1: exit(print(1))
    if C-c > 0 and (C-c)*2 >= N-i-1: exit(print(1))

print(2)