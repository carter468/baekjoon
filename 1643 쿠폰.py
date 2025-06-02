# 쿠폰
# Gold 5, implementation, math, probability, linearity of expectation

def gcd(a,b):
    while b:
        a,b = b,a%b
    return a

while True:
    try: N = int(input())
    except: break

    x = 1
    for i in range(2,N):
        x = x*i//gcd(x,i)

    y = 0
    for i in range(1,N+1):
        y += N*x//i
    
    g = gcd(y,x)
    y //= g
    x //= g
    z,y = divmod(y,x)

    if y == 0: print(z)
    else:
        l = len(str(z))
        print(' '*l,y)
        print(z,'-'*len(str(x)))
        print(' '*l,x)