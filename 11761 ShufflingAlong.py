# Shuffling Along
# Gold 5, implementation, simulation

n,m = input().split()
n = int(n)

s = list(range(n))
t = list(range(n))
count = 0
while True:
    count += 1
    if n%2 == 0:
        a,b = t[:n//2],t[n//2:]
        if m == 'in': a,b = b,a
        t = []
        for i in range(n//2):
            t.append(a[i])
            t.append(b[i])
    else:
        if m == 'in':
            a,b = t[:n//2],t[n//2:]
            t = []
            for i in range(n//2):
                t.append(b[i])
                t.append(a[i])
            t.append(b[-1])
        else:
            a,b = t[:n//2+1],t[n//2+1:]
            t = []
            for i in range(n//2):
                t.append(a[i])
                t.append(b[i])
            t.append(a[-1])
    if t == s: break
print(count)