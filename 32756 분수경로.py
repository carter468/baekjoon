# 분수 경로
# Gold 4, bitmask, constructive, ad hoc

def gcd(x,y):
    while y:
        x,y = y,x%y
    return x

n,d = map(int,input().split())

result = ''
f = n < 0
if n < 0: n *= -1

g = gcd(n,d)
n //= g
d //= g

c = 0
while d > 1:
    if d%2 != 0:
        print(-1)
        exit()
    d //= 2
    c += 1

b = bin(n)[2:]
l = len(b)
if l > c:
    for i in range(l-c):
        if b[-1-c-i] == '1':
            result += 'RL'[f]
        result += 'U'
    result += 'D'*(l-c+1)
    for i in range(c):
        if b[-c+i] == '1':
            result += 'RL'[f]
        result += 'D'
else:
    b = b.zfill(c)
    result = 'D'
    for i in range(c):
        if b[i] == '1':
            result += 'RL'[f]
        result += 'D'

print(len(result))
print(result)