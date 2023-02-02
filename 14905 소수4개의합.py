# 소수 4개의 합
# Gold 3, 골드바흐의 추측

import sys

def is_prime(k):   
    for i in range(3,int(k**0.5)+1,2):
        if k%i==0:
            return False
    return True

while True:
    try:
        n = int(sys.stdin.readline())

        if n<8:
            print('Impossible.')
            continue

        if n%2:
            print(2,3,end=' ')
            n -= 5
        else:
            print(2,2,end=' ')
            n -= 4

        if n==4:
            print(2,2)
            continue

        for i in range(3,n,2):
            if is_prime(i) and is_prime(n-i):
                print(i,n-i)
                break

    except:
        break