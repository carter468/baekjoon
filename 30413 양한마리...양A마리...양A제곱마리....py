# 양 한 마리... 양 A마리... 양 A제곱마리...
# Gold 3, math, flt, exponentiation by squaring

M = 10**9+7

def pow(x,y):
    if y == 1: return x
    z = pow(x,y//2)
    if y%2 == 0: return z*z%M
    else: return z*z*x%M

a,b = map(int,input().split())
if a == 1: print(b%M)
else: print((pow(a,b)-1)*pow(a-1,M-2)%M)

# 내장함수사용코드

# M = 10**9+7

# a,b = map(int,input().split())
# if a == 1: print(b%M)
# else: print((pow(a,b,M)-1)*pow(a-1,M-2,M)%M)