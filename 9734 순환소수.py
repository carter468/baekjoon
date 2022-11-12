# 순환소수
import sys

while True:
    try:
        x = sys.stdin.readline().strip()
        a,e = x.split('.')   
        a = int(a)  # 정수부분
        b,c = e[:-1].split('(')    # 순환하지 않는 부분, 순환하는 부분
        d = int(b) if b else 0     # 순환하지 않는 부분
        f = int('9'*len(c)+'0'*len(b))  # 분모
        g = int(b+c)-d # 분자

        # 유클리드 호제법
        h,i = f,g
        while i!=0:
            h,i = i,h%i

        # 기약분수
        f //= h
        g //= h
        g += a * f
        print(f'{x} = {g} / {f}')
    except EOFError:
        break