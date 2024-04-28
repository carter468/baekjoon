# 헨리
# Gold 5, math

def gcd(a,b):
    while b != 0:
        a,b = b,a%b
    return a

for _ in range(int(input())):
    a,b = map(int,input().split())
    while a != 1:
        c = int(b//a)+1
        d = b*c
        e = a*c-b
        g = gcd(d,e)
        b = d//g
        a = e//g
    print(b)