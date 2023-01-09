# 소수를 분수로
# Silver 1, 파싱, 유클리드 호제법, 수학

import sys
input = sys.stdin.readline

def gcd(a,b):
    while b!=0:
        a,b = b,a%b
    return a
    
for _ in range(int(input())):
    n = input().strip()[2:]
    if '(' in n:    # 순환소수
        a,b = n[:-1].split('(')
        p = int('9'*len(b)+'0'*len(a))
        if a:
            q = int(a+b)-int(a)
        else:
            q = int(b)
    else:       # 유한소수
        q = int(n)
        p = 10**len(n)
    g = gcd(p,q)
    print(f'{q//g}/{p//g}')