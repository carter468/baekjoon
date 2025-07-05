# 뛰는 기물
# Platinum 5, ad hoc

def gcd(a,b):
    while b:
        a,b = b,a%b
    return a

N,M = map(int,input().split())

g = gcd(N,M)
print(g*g*[2,1][(N+M)//g%2])