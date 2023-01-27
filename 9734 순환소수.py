# 순환소수
# Silver 1, 유클리드 호제법, 파싱, 수학

import sys

def GCD(m,n):
    while n!=0:
        m,n = n,m%n
    return m

while True:
    try:
        a = sys.stdin.readline().strip()
        x,b = a.split('.')
        y,z = b[:-1].split('(')
        p = int('9'*len(z)+'0'*len(y))
        q = int(x+y+z)-int(x+y)
        g = GCD(p,q)
        print(f'{a} = {q//g} / {p//g}')

    except:
        break