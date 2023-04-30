# a^b
# Gold 5, 큰 수 연산

a,b = input().split()
x,y = a.split('.')
p = len(y)
c = str(int(x+y)**int(b))
d = p*int(b)
if x == '0':
    print('0.'+c.zfill(d))
else:
    print(c[:-d]+'.'+c[-d:])