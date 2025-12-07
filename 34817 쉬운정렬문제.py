# 쉬운 정렬 문제
# Gold 5, ad hoc

N,K = map(int,input().split())
A = tuple(map(int,input().split()))

m = 0
for a in A:
    if m > a+K:
        print('NO')
        break
    m = max(m,a)
else: print('YES')