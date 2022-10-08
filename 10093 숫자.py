# 숫자

a,b = map(int,input().split())
if a > b:
    a,b = b,a
if a == b:
    n = 0
else:
    n = b-a-1
print(n)
for i in range(a+1,b):
    print(i,end=' ')