# 등비수열의 합
# Gold 3, bruteforcing, math

N = int(input())

for r in range(2,int(N**0.5)+1):
    n = 3
    while r**(n-1) < N:
        if N*(r-1)%(r**n-1) == 0:
            a = N*(r-1)//(r**n-1)
            print(n)
            for _ in range(n):
                print(a,end=' ')
                a *= r
            exit()
        n += 1
print(-1)