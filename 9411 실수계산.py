# 실수 계산
# Gold 3, 임의정밀도 / 큰수계산

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    a,b = 0,0

    while ((f:=input().strip()) != '0'):
        n = f.split('.')
        s = -1 if f[0] == '-' else 1
        if len(n) == 1:
            c,d = int(n[0]),0
        else:
            c,d = int(n[0]),int(n[1]+'0'*(29-len(n[1])))
        a += c
        b += d*s
    
    s = -1 if b < 0 else 1
    b *= s
    b = str(b)

    if len(b) > 29:
        a += int(b[:len(b)-29])*s
        b = int(b[-29:])
    else:
        b = int(b)

    k = '-' if a < 0 or a == 0 and s < 0 else ''
    if a > 0 and s < 0 and b != 0:
        a -= 1
        b = 10**29-b
    elif a < 0 and s > 0 and b != 0:
        a += 1
        b = 10**29-b

    b = '0'*(29-len(str(b)))+str(b)

    while b and b[-1] == '0':
        b = b[:-1]

    a = k+str(abs(a))
    print(a+'.'+b if b else a)