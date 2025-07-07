# 타일 뒤집기 (Easy)
# Gold 4, simulation

def f(x):
    return '.' if x == '#' else '#'

N = int(input())
b = list(input())

a = '.'*N
for _ in range(N):
    print(''.join(b))
    c = []
    for i in range(N):
        k = '.'
        if a[i] == '#': k = f(k)
        for j in (i-1,i+1):
            if 0 <= j < N and b[j] == '#': k = f(k)
        c.append(k)
    a,b = b,c