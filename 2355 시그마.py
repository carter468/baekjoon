# 2355 시그마

a,b = map(int,input().split())
if a>b:
    a,b = b,a
max_value = 2147483648
x = (a+b)*(b-a+1)//2
if x>=max_value:
    print(max_value-1)
elif x<max_value*-1:
    print(max_value*-1)
else:
    print(x)