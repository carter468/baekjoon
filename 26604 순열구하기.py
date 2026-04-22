# 순열 구하기
# Gold 2, implementation

N = int(input())
B = list(map(int,input().split()))

s = set(range(1,N+1))
for i in range(1,N+1):
    c = 0
    a = 1
    while c <= N-i:
        while a not in s:
            a += 1
        B[c] ^= a
        c += 1
        a += 1
    s.remove(B[-i])
print(*B)