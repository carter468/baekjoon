# 신기한 소수
# Gold 5, 백트래킹, 소수판정

def isPrime(x):
    if x == 1: return False
    i = 2
    while i*i <= x:
        if x%i == 0:
            return False
        i += 1
    return True

def bt(x,l):
    if not isPrime(x): return
    if l == n:
        print(x)
        return
    for i in range(1,10):
        bt(x*10+i,l+1)

n = int(input())
bt(0,0)