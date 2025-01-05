# X와 K
# Gold 4, math

x,k = map(int,input().split())

answer = 0
a = 1
while k:
    while x%2:
        x >>= 1
        a <<= 1
    answer += a*(k%2)
    k >>= 1
    x >>= 1
    a <<= 1
print(answer)