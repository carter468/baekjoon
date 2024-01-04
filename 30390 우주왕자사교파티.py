# 우주왕자 사교파티
# Gold 3, math, number theory

a,b,k = map(int,input().split())

c = a+b
a = min(a,b)
f = []
for i in range(1,int(c**0.5)+1):
    if c%i == 0:
        f.append(i)
        f.append(c//i)

for i in sorted(f):
    x = c//i
    r = a%x
    if min(r,x-r) <= k:
        print(x)
        break