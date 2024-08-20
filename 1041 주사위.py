# 주사위
# Gold 5, greedy

n = int(input())
a,b,c,d,e,f = map(int,input().split())

x = min(a+b+c,a+b+d,a+d+e,a+c+e,f+b+c,f+b+d,f+d+e,f+c+e)
y = min(a+b,a+d,a+c,a+e,f+b,f+c,f+d,f+e,b+d,d+e,e+c,c+b)
m = min(a,b,c,d,e,f)

if n == 1: print(a+b+c+d+e+f-max(a,b,c,d,e,f))
else: print(x*4+y*(4+(n-2)*8)+m*(n*n*5-(4*3+(4+(n-2)*8)*2)))
