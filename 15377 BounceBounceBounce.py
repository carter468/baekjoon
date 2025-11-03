# Bounce Bounce Bounce
# Gold 1, euler phi

import sys
input = sys.stdin.readline

def phi(n):
    result = n
    for i in range(2,int(n**0.5)+1):
        if n%i == 0:
            result = result*(i-1)//i
            while n%i == 0: n //= i
    if n > 1: result = result*(n-1)//n
    return result

for _ in range(int(input())):
    print(phi(int(input())+1))