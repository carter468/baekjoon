# 약속 시간
# Gold 1, math, probability, caclculus

def gcd(a,b):
    while b:
        a,b = b,a%b
    return a

M = int(input())

a = M**3+M**2*(60-M)*3
b = 60**3
g = gcd(a,b)
print(f'{a//g}/{b//g}')