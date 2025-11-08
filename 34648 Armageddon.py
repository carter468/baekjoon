# Armageddon 
# Gold 2, greedy, modular multiplicative inverse, FLT

MOD = 10**9+7

p,q,n = map(int,input().split())

k = pow(q,-1,MOD)
result = [0]
if n > 1:
    result.append(1)
    x = y = 1
    a = b = 1
    for i in range(3,n+1):
        if x != y:
            a = a*(y+2)%MOD
            b = b*pow(y,-1,MOD)%MOD
            y += 1
        else:
            if (x+2)*q > x*p:
                a = a*(x+2)%MOD
                b = b*pow(x,-1,MOD)%MOD
                x += 1
            else:
                a = a*p%MOD
                b = b*k%MOD
        result.append(a*b%MOD)
print(*result)