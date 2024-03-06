# 갈래 제곱
# Gold 1, implementation, parsing 

def gcd(x,y):
    while y: x,y = y,x%y
    return x

for _ in range(int(input())):
    a,b = input().split()

    if a[0] == 'C' and b == '0':
        print('Yes')
        continue
    
    arr1,arr2 = [0]*501,[0]*501
    if a[0] != 'C':
        i = 0
        while a[i+1] != 'C':
            t = ''
            while a[i] != 'x':
                t += a[i]
                i += 1
            if not t: p,q = 1,1
            elif t in '-+': p,q = int(t+'1'),1
            elif '/' in t: p,q = map(int,t.split('/'))
            else: p,q = int(t),1
            i += 2
            t = ''
            while a[i] not in '+-':
                t += a[i]
                i += 1
            r = int(t)
            p *= r*(r-1)
            g = gcd(p,q)
            p //= g
            q //= g
            if q < 0: p,q = -p,-q
            arr1[r-2] = (p,q)

    i = 0
    while i < len(b):
        r = 1
        t = ''
        while i < len(b) and b[i] != 'x':
            t += b[i]
            i += 1
        if i < len(b):
            if not t: p,q = 1,1 
            elif t in '-+': p,q = int(t+'1'),1
            elif '/' in t: p,q = map(int,t.split('/'))
            else: p,q = int(t),1
        else:
            if '/' in t: p,q = map(int,t.split('/'))
            else: p,q = int(t),1 
            arr2[0] = (p,q)
            break
        if i+1 < len(b) and b[i+1] == '^':
            i += 2
            t = ''
            while i < len(b) and b[i] not in '+-':
                t += b[i]
                i += 1
            r = int(t)
        else:
            r = 1
            i += 1
        arr2[r] = (p,q)
    print('Yes' if arr1 == arr2 else 'No')