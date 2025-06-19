# 타율 분석
# Gold 3, probability

def nCr(n,r):
    x = 1
    for i in range(r):
        x = x*(n-i)//(i+1)
    return x

A,B = input().split()
A,B = float(A),int(B)

p = 0
for i in range(B+1):
    p += A**i*(1-A)**(B-i)*nCr(B,i)
    if p >= 0.05:
        exit(print(i))