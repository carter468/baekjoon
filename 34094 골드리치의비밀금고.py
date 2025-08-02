# 골드리치의 비밀 금고
# Gold 5, ad hoc, constructive

input()
A = sorted(map(int,input().split()))

if set(A) == {0}:
    print(0)
else:
    x = 0
    for a in A:
        if a == x: x += 1
        elif a != x-1: break
    print(x+1)
print(*A)