# 이음줄
# Gold 4, geometry

a,b = map(float,input().split())

c = (a*a+b*b)**0.5
d = abs((c-a)**2-b*b)/2/b
e = (a*a+d*d)**0.5
f = a*(b-d)/e

print(f'{e/2:.2f} {f:.2f}')