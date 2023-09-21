# n제곱 계산
# Platinum 1, math, exponentiation by squaring

def mul(a,b):
    c = a[0]*b[0]+a[1]*b[1]*5
    d = a[0]*b[1]+a[1]*b[0]
    return c%1000,d

def pow(a,p):
    if p == 1: return a
    b = pow(a,p//2)
    if p%2 == 0: return mul(b,b)
    else: return mul(mul(b,b),a)

for i in range(int(input())):
    n = int(input())
    x = pow((3,1),n)[0]+pow((3,-1),n)[0]-1
    print(f'Case #{i+1}: {str(x%1000).zfill(3)}')