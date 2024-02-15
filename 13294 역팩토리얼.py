# 역팩토리얼
# Gold 3, stirling's approximation

from math import log,pi

n = input()

if len(n) < 19:
    n = int(n)
    x = 1
    for i in range(1,99):
        x *= i
        if x == n:
            print(i)
            break
else:       
    n = log(int(n[:10]))+(len(n)-10)*log(10)
    for i in range(1,10**9):
        x = i*log(i)-i+log(2*pi*i)/2
        if x-n > -1: break
    print(i)