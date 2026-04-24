# The Sparsest Number in Between
# Gold 5, bitmask, greedy

A,B = map(int,input().split())

m = bin(A).count('1')
arr = [A]

l = 61
d = 0
for i in range(l):
    if A>>(l-i-1)&1 == 1:
        d += 1<<(l-i-1)
        x = d
    else:
        x = d+(1<<(l-i-1))
    if A < x <= B:
        c = bin(x).count('1')
        if c < m:
            m = c
            arr = [x]
        elif c == m:
            arr.append(x)
print(sorted(arr)[0])