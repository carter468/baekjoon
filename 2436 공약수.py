# 공약수
# Gold 5, 정수론

def gcd(a,b):
    while b:
        a,b = b,a%b
    return a

a,b  = map(int,input().split())

c = b//a
for i in range(int(c**0.5),1,-1):
    if c%i==0 and gcd(a*i,a*c//i)==a:
        print(a*i,a*c//i)
        break
else:
    print(a,b)