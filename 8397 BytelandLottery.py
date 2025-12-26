# Byteland Lottery
# Platinum 5, number theory, combinatorics

def f(x):
    return x if x < 10 else (x-1)%9+1

input()
r = 0
for a in map(int,input().split()):
    r = f((r+1)*(f(a)+1)-1)
print(r)