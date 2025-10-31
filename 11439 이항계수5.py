# 이항 계수 5
# Platinum 4, number theory, seive, prime factorization

def count(n,p):
    c = 0
    a = p
    while a <= n:
        c += n//a
        a *= p
    return c

N,K,M = map(int,input().split())

seive = [True]*(N+1)
for i in range(2,int(N**0.5)+1):
    if seive[i]:
        for j in range(i*i,N+1,i):
            seive[j] = False

result = 1
for i in range(2,N+1):
    if seive[i]:
        c = count(N,i)-count(N-K,i)-count(K,i)
        result = result*pow(i,c,M)%M
print(result)