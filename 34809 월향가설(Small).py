# 월향 가설 (Small)
# Platinum 4, number theory

def solve(x):
    while True:
        for i in range(int(x**0.5)+1):
            a = x-i*i
            if (int(a**0.5))**2 == a:
                print(i,int(a**0.5))
                return
        x += p

N = int(input())
A = tuple(map(int,input().split()))

p = 1000003
print(p)
for a in A:
    solve(a)