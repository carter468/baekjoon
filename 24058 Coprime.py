# Coprime
# Gold 1, number theory, inclusion and exclusion

N,K = map(int,input().split())

n = N
factor = set()
i = 2
while i*i <= n:
    while n%i == 0:
        n //= i
        factor.add(i)
    i += 1
if n > 1: factor.add(n)
factor = list(factor)

result = 0
n = len(factor)
for i in range(1<<n):
    c = 1
    x = 1
    for j in range(n):
        if i>>j&1:
            c *= -1
            x *= factor[j]
    k = N*K//x
    result += k*(k+1)//2*x*c
print(result)