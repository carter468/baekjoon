# K개의 소수
# Gold 3, case work, number theory, constructive

def isprime(n):
    if n == 2: return True
    if n < 2 or n%2 == 0: return False
    for i in range(3,int(n**0.5)+1,2):
        if n%i == 0: return False
    return True

def solve(n):
    i = 2
    while True:
        if isprime(i) and isprime(n-i): return i,n-i
        i += 1

N,K = map(int,input().split())
if K == 1:
    print(N if isprime(N) else -1)
elif K == 2:
    if N%2 == 0:
        if N >= 4:
            print(*solve(N))
        else:
            print(-1)
    else:
        if isprime(N-2):
            print(2,N-2)
        else:
            print(-1)
else:
    a = [2]*(K-2)
    N -= 2*(K-2)
    a[0] += N%2
    N -= N%2
    if N >= 4:
        print(*a,*solve(N))
    else:
        print(-1)