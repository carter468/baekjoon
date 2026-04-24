# Show Me The Operators
# Gold 5, implementation

for tc in range(int(input())):
    s = input().split()
    t = [int(s[0])]
    r = []
    for i in range(len(s)//2):
        a = s[i*2+1]
        b = int(s[i*2+2])
        if a == '/':
            t[-1] //= b
            r.append(a)
        elif a == '*':
            t[-1] *= b
            r.append(a)
        else:
            t.extend([a,b])
    
    x = t[0]
    for i in range(len(t)//2):
        a,b = t[i*2+1],t[i*2+2]
        if a == '+':
            x += b
        else:
            x -= b
        r.append(a)
    print(f'Case #{tc+1}:',*r,x)