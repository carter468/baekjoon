# 걸어가요
# Gold 3, number theory, CRT

import math

a,b = 0,1
m = 0
for _ in range(int(input())):
    c,d = map(int,input().split())
    g = math.gcd(b,d)
    if (c-a)%g != 0:
        exit(print(-1))
    t = (c-a)//g*pow(b//g,-1,d//g)%(d//g)
    a += b*t
    b *= d//g
    a %= b
    m = max(m,c)
if a < m:
    a += (m-a+b-1)//b*b
print(a)