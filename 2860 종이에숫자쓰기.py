# 종이에 숫자 쓰기
# Gold 4, number theory

def gcd(m,n):
    while n != 0:
        m,n = n,m%n
    return m

a,b = input().split('.')
c = 10**(len(b))
a,b = int(a),int(b)

if b == 0:
    print(*[0]*(a-1),1,*[0]*(5-a))
else:
    g = gcd(b,c)
    x,y = c//g,b//g
    print(*[0]*(a-1),x-y,y,*[0]*(5-a-1))