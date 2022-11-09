# 에라토스테네스의 체

def solve():
    n,k = map(int,input().split())
    prime = [True]*(n+1)
    count = 0
    for i in range(2,n+1):
        if prime[i]:
            count += 1
            if count == k:
                return i
            for j in range(i*2,n+1,i):
                if prime[j]:
                    count += 1
                    if count == k:
                        return j
                prime[j] = False

print(solve())