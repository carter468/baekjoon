# 조화평균

n = input()
arr = list(map(int,input().split()))

def gcd(a,b):
    if b == 0:
        return a
    a,b = b,a%b
    return gcd(a,b)

def lcm(a,b):
    return a*b//gcd(a,b)

x = 1
for a in arr:
    x = lcm(a,x)
y = 0
for a in arr:
    y += x//a
g = gcd(x,y)
x //= g
y //= g
print(f'{x}/{y}')