# 곱셈

def p(b):   #지수 분할
    global a,c
    if b == 1:
        return a%c
    elif b == 2:
        return (a**2)%c
    else:           
        if b%2==0:  # 지수가 짝수
            return (p(b//2)**2)%c
        else:       # 지수가 홀수
            return (((p((b-1)//2))**2)*a)%c

a,b,c = map(int,input().split())
print(p(b))