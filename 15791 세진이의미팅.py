# 세진이의 미팅
# Gold 1, fermat's little theorem

def pow(x,y):
    if y == 1: return x
    z = pow(x,y//2)
    if y%2 == 0: return z*z%M
    else: return z*z*x%M

M = 10**9+7

n,m = map(int,input().split())

m = min(m,n-m)
a,b = 1,1
for i in range(m):
    a = a*(n-i)%M
    b = b*(i+1)%M
    
print(a*pow(b,M-2)%M)