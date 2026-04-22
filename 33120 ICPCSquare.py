# ICPC Square
# Platinum 5, number theory

N,D,S = map(int,input().split())

n = N//S
d = D//S
if n-1 <= d:
    exit(print(n*S))
x = min(n,d*2)
if x-1 <= d:
    exit(print(x*S))
for i in range(2,int(x**0.5)+1):
    if x%i == 0 and x-x//i <= d:
        exit(print(x*S))
print((x-1)*S)