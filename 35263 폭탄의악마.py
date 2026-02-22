# 폭탄의 악마
# Gold 3, difference array, probability, number theory

M = 500000
sieve = [True]*M
prime = []
for i in range(2,int(M**0.5)+1):
    if sieve[i]:
        prime.append(i)
        for j in range(i*i,M,i):
            sieve[j] = False

N,M = map(int,input().split())
A = tuple(map(int,input().split()))

arr = [0]*(N+1)
for _ in range(M):
    i,j = map(int,input().split())
    arr[i-1] += 1
    arr[j] -= 1

result = 0
for i in range(N):
    a = A[i]
    arr[i+1] += arr[i]
    if arr[i] > 0:
        f = set()
        for p in prime:
            while a%p == 0:
                f.add(p)
                a //= p
        if a > 1: f.add(a)
        result += sum(f)/len(f)
    else:
        result += a
print(result)